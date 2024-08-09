# import json
# import networkx as nx
# import matplotlib.pyplot as plt

# # The JSON data as a string
# jsonString = '''
# {
#     "": "[]",
#     "rest/admin/application-configuration": "['/api/Users/', '/rest/user/']",
#     "socket.io": "[]",
#     "rest/admin/application-version": "['/api/Users/', '/rest/user/']",
#     "api/Challenges": "['/api/Users/', '/rest/user/']",
#     "rest/languages": "['/api/Users/', '/rest/user/']",
#     "api/Quantitys": "['/api/Cards/', '/api/Challenges/', '/api/Addresss', '/rest/products/search', '/api/Complaints/', '/rest/saveLoginIp', '/api/Feedbacks/', '/api/Cards', '/api/Addresss/']",
#     "rest/products/search": "['/api/Cards/', '/api/Challenges/', '/api/Addresss', '/api/Complaints/', '/rest/saveLoginIp', '/api/Feedbacks/', '/api/Quantitys/', '/api/Cards', '/api/Addresss/']",
#     "font-mfizz.woff": "[]",
#     "api/SecurityQuestions": "[]",
#     "api/Users": "[]",
#     "api/SecurityAnswers": "[]",
#     "rest/user/whoami": "['/api/Users/', '/rest/user/']",
#     "rest/user": "[]",
#     "rest/basket/{id}": "['/api/Users/', '/rest/user/']",
#     "rest/products/{id}/reviews": "['/api/Users/', '/rest/user/', '/rest/products/reviews']",
#     "rest/products/reviews": "['/api/Users/', '/rest/user/']",
#     "api/BasketItems": "['/api/Users/', '/rest/user/']",
#     "api/Products/{id}": "['/api/Users/', '/rest/user/']",
#     "api/BasketItems/{id}": "['/api/Users/', '/rest/user/', '/api/BasketItems/']",
#     "profile": "[]",
#     "profile/image/file": "['/profile']",
#     "rest/order-history": "['/api/Users/', '/rest/user/']",
#     "api/Recycles": "['/api/Users/', '/rest/user/']",
#     "api/Addresss": "['/api/Users/', '/api/Challenges/', '/rest/products/search', '/rest/user/', '/api/Quantitys/', '/api/Addresss/']",
#     "api/Cards": "['/api/Cards/', '/api/Users/', '/api/Challenges/', '/api/Addresss', '/rest/products/search', '/api/Complaints/', '/rest/user/', '/api/Feedbacks/', '/api/Quantitys/', '/api/Addresss/']",
#     "rest/wallet/balance": "['/api/Users/', '/rest/user/']",
#     "rest/continue-code": "['/api/Users/', '/rest/user/']",
#     "rest/user/change-password": "['/api/Users/', '/rest/user/']",
#     "rest/2fa/status": "['/api/Users/', '/rest/user/']",
#     "rest/captcha": "['/api/Users/', '/rest/user/']",
#     "api/Feedbacks": "['/api/Users/', '/api/Challenges/', '/api/Addresss', '/rest/products/search', '/api/Complaints/', '/rest/user/', '/api/Quantitys/', '/api/Addresss/']",
#     "api/Complaints": "['/api/Users/', '/api/Challenges/', '/api/Addresss', '/rest/products/search', '/rest/user/', '/api/Feedbacks/', '/api/Quantitys/', '/api/Addresss/']",
#     "rest/chatbot/status": "['/api/Users/', '/rest/user/', '/rest/chatbot/respond']",
#     "rest/chatbot/respond": "['/api/Users/', '/rest/chatbot/status', '/rest/user/']",
#     "rest/memories": "['/api/Users/', '/rest/user/']",
#     "assets/public/images/uploads/%F0%9F%98%BC-": "[]",
#     "rest/deluxe-membership": "['/api/Users/', '/rest/user/']",
#     "rest/saveLoginIp": "['/api/Cards/', '/rest/2fa/status', '/api/Users/', '/api/Challenges/', '/api/Addresss', '/rest/products/search', '/api/Complaints/', '/rest/user/', '/api/Feedbacks/', '/api/Quantitys/', '/api/Cards', '/api/Addresss/']"
# }
# '''

# # Load the JSON data
# data = json.loads(jsonString)

# # Create a directed graph
# G = nx.DiGraph()

# # Add edges to the graph based on the JSON data
# for parent, children_str in data.items():
#     children = json.loads(children_str.replace("'", "\""))
#     for child in children:
#         # Remove leading/trailing slashes for consistency
#         clean_child = child.strip('/')
#         G.add_edge(parent, clean_child)

# # Draw the graph
# plt.figure(figsize=(15, 10))
# pos = nx.spring_layout(G, k=0.5, iterations=20)  # Position nodes using Fruchterman-Reingold force-directed algorithm
# nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="#707070", linewidths=1, arrows=True)
# plt.title("API Dependencies Tree")
# plt.show()

import sqlite3
from graphviz import Digraph
from collections import defaultdict

# Function to generalize paths with IDs
def generalize_path(path):
    generalized_path = []
    for part in path.split('/'):
        if part.isdigit():
            generalized_path.append('{id}')
        else:
            generalized_path.append(part)
    return '/'.join(generalized_path)

# Function to build the dependency tree
def build_dependency_tree(endpoints):
    tree = defaultdict(dict)
    for path, dependencies in endpoints.items():
        # Generalize the path
        generalized_path = generalize_path(path)
        # Add dependencies as child nodes
        for dep in dependencies:
            generalized_dep = generalize_path(dep)
            tree[generalized_path][generalized_dep] = {}
    return tree

# Connect to the SQLite database
def connect_to_db():
    return sqlite3.connect('db.sqlite3')

# Fetch data from the database
def fetch_endpoints_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT path, dependency_list FROM dependency_app_endpoints")
    rows = cursor.fetchall()
    
    endpoints_data = {}
    for row in rows:
        path, dependencies = row
        dependencies = eval(dependencies)  # Convert string representation to list
        endpoints_data[path] = dependencies
    return endpoints_data

# Visualize the dependency tree using Graphviz
def visualize_tree(dependency_tree):
    dot = Digraph(comment='API Dependency Tree')

    # Function to add nodes and edges to the graph
    def add_nodes_edges(tree, parent=None):
        for key, subtree in tree.items():
            if parent is None:
                dot.node(key, key)
            else:
                dot.node(key, key)
                dot.edge(parent, key)
            add_nodes_edges(subtree, key)

    # Adding nodes and edges to the graph
    add_nodes_edges(dependency_tree)

    # Render the graph
    dot.render('final-8', format='png', cleanup=True)

def main():
    conn = connect_to_db()
    endpoints_data = fetch_endpoints_data(conn)
    conn.close()
    
    # Build the dependency tree
    dependency_tree = build_dependency_tree(endpoints_data)
    
    # Visualize the tree
    visualize_tree(dependency_tree)

if __name__ == '__main__':
    main()
