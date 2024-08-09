from haralyzer import HarParser, HarPage
import json

def load_and_parse_har(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        har_data = json.load(file)
    har_parser = HarParser(har_data)
    return har_parser.har_data

har_parser = load_and_parse_har('Juiceshop1.har')

def extract_requests_responses(har_parser):
    requests = []
    responses = []
    entries = har_parser['log']['entries']

    for entry in entries:
        request = entry['request']
        response = entry['response']
        requests.append({
            'url': request['url'],
            'method': request['method'],
            'headers': request['headers'],
            'queryString': request.get('queryString', []),
            'postData': request.get('postData', {})
        })
        responses.append({
            'status': response['status'],
            'headers': response['headers'],
            'content': response['content']
        })

    return requests, responses

requests, responses = extract_requests_responses(har_parser)

def find_dependencies(requests, responses):
    dependencies = []
    url_to_index = {req['url']: idx for idx, req in enumerate(requests)}

    for idx, req in enumerate(requests):
        for param in req['queryString']:
            dependent_url = param['value']  # Example of how to identify dependency
            if dependent_url in url_to_index:
                dependencies.append((url_to_index[dependent_url], idx))

    return dependencies

dependencies = find_dependencies(requests, responses)

import networkx as nx
import matplotlib.pyplot as plt

def create_dependency_tree(dependencies):
    G = nx.DiGraph()

    for idx, req in enumerate(requests):
        G.add_node(idx, url=req['url'])

    for dep in dependencies:
        G.add_edge(dep[0], dep[1])

    return G

G = create_dependency_tree(dependencies)

def visualize_dependency_tree(G):
    pos = nx.spring_layout(G)
    labels = {i: data['url'] for i, data in G.nodes(data=True)}
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=3000, node_color="skyblue", font_size=10)
    plt.show()

visualize_dependency_tree(G)
