# import sqlite3
# from graphviz import Digraph
# from collections import defaultdict

# # Function to generalize paths with IDs
# def generalize_path(path):
#     generalized_path = []
#     for part in path.split('/'):
#         if part.isdigit():
#             generalized_path.append('{id}')
#         else:
#             generalized_path.append(part)
#     return '/'.join(generalized_path)

# # Function to build the dependency tree and extract execution flow
# def build_execution_flow(endpoints):
#     tree = defaultdict(dict)
#     execution_flow = []
#     for path, dependencies in endpoints.items():
#         generalized_path = generalize_path(path)
#         # Skip paths that contain '{id}'
#         if '{id}' in generalized_path:
#             continue
#         execution_flow.append((generalized_path, [generalize_path(dep) for dep in dependencies if '{id}' not in dep]))
#         for dep in dependencies:
#             generalized_dep = generalize_path(dep)
#             if '{id}' not in generalized_dep:
#                 tree[generalized_path][generalized_dep] = {}
#     return tree, execution_flow

# # Connect to the SQLite database
# def connect_to_db():
#     return sqlite3.connect('db.sqlite3')

# # Fetch data from the database
# def fetch_endpoints_data(conn):
#     cursor = conn.cursor()
#     cursor.execute("SELECT path, dependency_list FROM dependency_app_endpoints")
#     rows = cursor.fetchall()
    
#     endpoints_data = {}
#     for row in rows:
#         path, dependencies = row
#         dependencies = eval(dependencies)  # Convert string representation to list
#         endpoints_data[path] = dependencies
#     return endpoints_data

# # Visualize the execution flow with dependencies using Graphviz
# def visualize_execution_flow_with_dependencies(execution_flow):
#     dot = Digraph(comment='API Execution Flow with Dependencies')

#     for i, (current_node, dependencies) in enumerate(execution_flow):
#         # Create node for the current endpoint
#         dot.node(current_node, current_node)

#         # Add edge from previous node to current node
#         if i > 0:
#             previous_node = execution_flow[i-1][0]
#             dot.edge(previous_node, current_node)
        
#         # Add nodes and edges for dependencies
#         for dep in dependencies:
#             dot.node(dep, dep)
#             dot.edge(current_node, dep)

#     # Render the graph
#     dot.render('api_execution_flow_with_dependencies', format='png', cleanup=True)

# def main():
#     conn = connect_to_db()
#     endpoints_data = fetch_endpoints_data(conn)
#     conn.close()
    
#     # Build the dependency tree and extract execution flow
#     dependency_tree, execution_flow = build_execution_flow(endpoints_data)
    
#     # Visualize the execution flow with dependencies
#     visualize_execution_flow_with_dependencies(execution_flow)

# if __name__ == '__main__':
#     main()

import sqlite3
from graphviz import Digraph
from collections import defaultdict #returns a default value rather than raising a keyerror

# Function to generalize paths with IDs
def generalize_path(path):
    generalized_path = []
    for part in path.split('/'):
        if part.isdigit():
            generalized_path.append('{id}')
        else:
            generalized_path.append(part)
    return '/'.join(generalized_path)

# Function to build the execution flow and dependency tree
def build_execution_flow(endpoints):
    tree = defaultdict(dict)
    execution_flow = []
    visited = set()

    def process_path(path, dependencies):
        generalized_path = generalize_path(path)
        if '{id}' in generalized_path or generalized_path in visited:
            return
        visited.add(generalized_path)
        refined_dependencies = []
        for dep in dependencies:
            generalized_dep = generalize_path(dep)
            if '{id}' not in generalized_dep and generalized_dep not in visited:
                tree[generalized_path][generalized_dep] = {}
                refined_dependencies.append(generalized_dep)
        execution_flow.append((generalized_path, refined_dependencies))

    for path, dependencies in endpoints.items():
        process_path(path, dependencies)

    return tree, execution_flow

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
        dependencies = eval(dependencies)  
        endpoints_data[path] = dependencies
    return endpoints_data

# Visualize the execution flow with dependencies using Graphviz
def visualize_execution_flow_with_dependencies(execution_flow):
    dot = Digraph(comment='API Execution Flow with Dependencies')

    for i, (current_node, dependencies) in enumerate(execution_flow):
        dot.node(current_node, current_node)

        if i > 0:
            previous_node = execution_flow[i-1][0]
            dot.edge(previous_node, current_node)
        
        for dep in dependencies:
            dot.node(dep, dep)
            dot.edge(current_node, dep)

    dot.render('refined_api_execution_flow', format='png', cleanup=True)

def main():
    conn = connect_to_db()
    endpoints_data = fetch_endpoints_data(conn)
    conn.close()
    
    # Build the dependency tree and extract execution flow
    dependency_tree, execution_flow = build_execution_flow(endpoints_data)
    
    # Visualize the execution flow with dependencies
    visualize_execution_flow_with_dependencies(execution_flow)

if __name__ == '__main__':
    main()
