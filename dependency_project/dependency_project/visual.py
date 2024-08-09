import json
import graphviz

def add_nodes_edges(graph, data, parent=None):
    if isinstance(data, dict):
        for key, value in data.items():
            graph.node(key)
            if parent:
                graph.edge(parent, key)
            add_nodes_edges(graph, value, key)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            node_name = f"{parent}_{index}"
            graph.node(node_name, label=f"Item {index}")
            if parent:
                graph.edge(parent, node_name)
            add_nodes_edges(graph, item, node_name)

def json_to_tree(json_file, output_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    graph = graphviz.Digraph(format='png')
    add_nodes_edges(graph, data)
    graph.render(output_file, view=True)

# Usage
json_to_tree('data.json', 'output_tree')
