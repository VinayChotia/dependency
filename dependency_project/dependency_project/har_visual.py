import json
import graphviz

def extract_requests(har_file):
    with open('Juiceshop1.har', 'r') as f:
        data = json.load(f)
    
    entries = data.get('log', {}).get('entries', [])
    requests = {}
    
    for entry in entries:
        request_url = entry['request']['url']
        response = entry.get('response', {})
        # Example dependency: assuming requests that have non-200 status codes are dependent
        if response.get('status') != 200:
            dependencies = [header.get('value') for header in entry.get('response', {}).get('headers', []) if 'Location' in header.get('name', '')]
            requests[request_url] = dependencies
    
    return requests

def build_dependency_tree(requests):
    graph = graphviz.Digraph(format='png')
    
    for request, dependencies in requests.items():
        graph.node(request)
        for dependency in dependencies:
            graph.node(dependency)
            graph.edge(request, dependency)
    
    return graph

def main(har_file, output_file):
    requests = extract_requests('Juiceshop1.har')
    tree = build_dependency_tree(requests)
    tree.render(output_file, view=True)

# Usage
main('Juiceshop1.har', 'dependency_tree')
