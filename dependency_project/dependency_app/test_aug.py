import json
import graphviz
from collections import defaultdict
from urllib.parse import urlparse


def parse_har(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        har_data = json.load(file)

    entries = har_data['log']['entries']
    sorted_entries = sorted(entries, key=lambda x: x['startedDateTime'])

    api_calls = []
    login_apis = []  # List to store multiple login APIs

    for entry in sorted_entries:
        request = entry['request']
        method = request['method']
        url = request['url']
        parsed_url = urlparse(url)
        path = parsed_url.path
        
        # Check if this is a login API
        if 'email' in request.get('postData', {}).get('text', '') and 'password' in request.get('postData', {}).get('text', ''):
            login_apis.append(path)

        api_calls.append((path, method))

    # Ensure at least one login API is found
    if not login_apis:
        raise ValueError("No login API found in the HAR file.")
    
    return login_apis, api_calls


def build_dependency_tree(api_calls, login_apis):
    tree = defaultdict(list)

    # Iterate over each login API
    for login_api in login_apis:
        parent = login_api
        visited = set()

        for path, method in api_calls:
            if path == login_api or path in visited:
                continue
            
            visited.add(path)
            tree[parent].append(path)
            parent = path

    return tree


def generate_graph(tree, output_file='dependency_tree'):
    dot = graphviz.Digraph(comment='API Dependency Tree')

    for parent, children in tree.items():
        for child in children:
            dot.edge(parent, child)

    dot.render(output_file, format='png')


# Test the functions with the HAR file
try:
    login_apis, api_calls = parse_har('Juiceshop1.har')
    dependency_tree = build_dependency_tree(api_calls, login_apis)
    generate_graph(dependency_tree)
except ValueError as e:
    print(f"Error: {e}")
