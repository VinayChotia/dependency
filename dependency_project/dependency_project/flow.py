# import sqlite3
# from graphviz import Digraph
# from collections import defaultdict

# def generalize_path(path):
#     generalized_path = []
#     for part in path.split('/'):
#         if part.isdigit():
#             generalized_path.append('{id}')
#         else:
#             generalized_path.append(part)
#     return '/'.join(generalized_path)

# def connect_to_db():
#     return sqlite3.connect('db.sqlite3')

# def fetch_endpoints_data(conn):
#     cursor = conn.cursor()
#     cursor.execute("SELECT path, dependency_list FROM dependency_app_endpoints")
#     rows = cursor.fetchall()
    
#     endpoints_data = {}
#     for row in rows:
#         path, dependencies = row
#         dependencies = eval(dependencies)  # Evaluate the stored list string back into a list
#         endpoints_data[path] = dependencies
#     return endpoints_data

# def parse_execution_flow_from_har(har_content):
#     execution_flow = []
#     entries = har_content['log']['entries']
#     for entry in entries:
#         request_info = entry['request']
#         path = request_info['url']
#         execution_flow.append(path)
#     return execution_flow

# def build_combined_tree(endpoints, execution_flow):
#     tree = defaultdict(dict)
#     previous_node = None
    
#     for path in execution_flow:
#         generalized_path = generalize_path(path)
        
#         if previous_node:
#             tree[previous_node][generalized_path] = {}

#         previous_node = generalized_path
        
#         for dep in endpoints.get(path, []):
#             generalized_dep = generalize_path(dep)
#             tree[generalized_path][generalized_dep] = {}
    
#     return tree

# def visualize_tree(dependency_tree):
#     dot = Digraph(comment='Combined API Dependency and Execution Flow Tree')

#     def add_nodes_edges(tree, parent=None):
#         for key, subtree in tree.items():
#             if parent is None:
#                 dot.node(key, key)
#             else:
#                 dot.node(key, key)
#                 dot.edge(parent, key)
#             add_nodes_edges(subtree, key)

#     add_nodes_edges(dependency_tree)
#     dot.render('final_combined_tree-2', format='png', cleanup=True)

# def main():
#     # Step 1: Connect to the database and fetch endpoint data
#     conn = connect_to_db()
#     endpoints_data = fetch_endpoints_data(conn)
#     conn.close()
    
#     # Step 2: Parse the HAR file to get the execution flow (Assuming har_content is already available)
#     har_content = {}  # Replace with actual HAR content loading
#     execution_flow = parse_execution_flow_from_har(har_content)
    
#     # Step 3: Build the combined tree
#     combined_tree = build_combined_tree(endpoints_data, execution_flow)
    
#     # Step 4: Visualize the combined tree
#     visualize_tree(combined_tree)

# if __name__ == '__main__':
#     main()

import sqlite3
from graphviz import Digraph
from collections import defaultdict

def generalize_path(path):
    generalized_path = []
    for part in path.split('/'):
        if part.isdigit():
            generalized_path.append('{id}')
        else:
            generalized_path.append(part)
    return '/'.join(generalized_path)

def connect_to_db():
    return sqlite3.connect('db.sqlite3')

def fetch_endpoints_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT path, dependency_list FROM dependency_app_endpoints")
    rows = cursor.fetchall()
    
    endpoints_data = {}
    for row in rows:
        path, dependencies = row
        dependencies = eval(dependencies)  
        endpoints_data[path] = dependencies
    return endpoints_data

def build_dependency_tree(endpoints):
    tree = defaultdict(dict)
    visited = set()
    
    def dfs(path, stack):
        generalized_path = generalize_path(path)
        stack.add(generalized_path)
        
        for dep in endpoints[path]:
            generalized_dep = generalize_path(dep)
            if generalized_dep in stack:
                print(f"Cycle detected: {generalized_path} -> {generalized_dep}")
                continue  # Skip adding this dependency to remove circular dependency
            if generalized_dep not in visited:
                tree[generalized_path][generalized_dep] = {}
                visited.add(generalized_dep)
                dfs(dep, stack)
        
        stack.remove(generalized_path)

    for path in endpoints:
        if generalize_path(path) not in visited:
            dfs(path, set())
            visited.add(generalize_path(path))
    
    return tree

def visualize_tree(dependency_tree):
    dot = Digraph(comment='API Dependency Tree')

    def add_nodes_edges(tree, parent=None):
        for key, subtree in tree.items():
            if parent is None:
                dot.node(key, key)
            else:
                dot.node(key, key)
                dot.edge(parent, key)
            add_nodes_edges(subtree, key)

    add_nodes_edges(dependency_tree)

    dot.render('final-7', format='png', cleanup=True)

def main():
    conn = connect_to_db()
    endpoints_data = fetch_endpoints_data(conn)
    conn.close()
    
    dependency_tree = build_dependency_tree(endpoints_data)
    
    visualize_tree(dependency_tree)

if __name__ == '__main__':
    main()
