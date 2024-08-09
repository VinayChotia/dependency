# import sqlite3
# import json

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

#     def add_child(self, child_node):
#         self.children.append(child_node)

#     def __repr__(self):
#         return f"TreeNode({self.value})"

# def load_data_from_db(db_path):
    
#     connection = sqlite3.connect(db_path)
#     cursor = connection.cursor()
#     cursor.execute('SELECT path, dependency_list FROM dependency_app_endpoints')
#     data = cursor.fetchall()
#     connection.close()
#     return data

# def create_nodes(data):
    
#     nodes = {}
#     for path, dep_list in data:
#         nodes[path] = TreeNode(path)
#     return nodes

# def build_tree(data, nodes):
    
#     for path, dep_list in data:
#         if dep_list:
#             dep_list_json = (dep_list)  
#             for dep in dep_list_json:
#                 if dep in nodes:
#                     nodes[path].add_child(nodes[dep])
#     return nodes

# def find_root(nodes):
   
#     all_nodes = set(nodes.keys())
#     child_nodes = set()
#     for node in nodes.values():
#         for child in node.children:
#             child_nodes.add(child.value)
#     root_nodes = list(all_nodes - child_nodes)
#     # if len(root_nodes) != 1:
#     #     raise ValueError("There should be exactly one root node, found: " + str(root_nodes))
#     return nodes[root_nodes[0]]


# if __name__ == "__main__":
#     db_path = "db.sqlite3"  
#     data = load_data_from_db(db_path)
#     nodes = create_nodes(data)
#     tree = build_tree(data, nodes)
#     root = find_root(nodes)
#     # print(f"Root: {root}")
#     print(tree)
    


# import sqlite3

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

#     def add_child(self, child_node):
#         self.children.append(child_node)

#     def __repr__(self):
#         return f"TreeNode({self.value})"

# def fetch_data_from_db(db_path):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
    
#     # Fetch all rows from the table
#     cursor.execute("SELECT path, dependency_list FROM dependency_app_endpoints")
#     rows = cursor.fetchall()
    
#     conn.close()
    
#     return rows

# def build_dict_of_dicts(rows):
#     data_dict = {}
    
#     for path, dep_list in rows:
#         dependencies = dep_list.split(',')  # Assuming comma-separated dependencies
#         data_dict[path] = [dep.strip() for dep in dependencies if dep.strip()]
    
#     return data_dict

# def build_tree_from_dict(data_dict):
#     nodes = {key: TreeNode(key) for key in data_dict.keys()}
    
#     for key, children in data_dict.items():
#         node = nodes[key]
#         for child_key in children:
#             if child_key in nodes:
#                 child_node = nodes[child_key]
#                 node.add_child(child_node)
    
#     return nodes

# def print_tree(node, level=0):
#     indent = " " * (level * 4)
#     print(f"{indent}{node.value}")
#     for child in node.children:
#         print_tree(child, level + 1)

# # Main execution
# if __name__ == "__main__":
#     # Path to the SQLite database file
#     db_path = 'db.sqlite3'
    
#     # Fetch data from the database
#     rows = fetch_data_from_db(db_path)
#     print(rows)
    
#     # Build the dictionary of dependencies
#     data_dict = build_dict_of_dicts(rows)
    
#     # Build the tree
#     nodes = build_tree_from_dict(data_dict)
    

#     root = nodes.get('/')
    
#     # Print the tree
#     if root:
#         print(root.value)

# ye infinite jaa raha hai abhi
# import sqlite3
# import sys

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(300)

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

#     def add_child(self, child_node):
#         self.children.append(child_node)

#     def __repr__(self):
#         return f"TreeNode({self.value})"

# def fetch_data_from_db(db_path):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
    

#     cursor.execute("SELECT path, dependency_list FROM dependency_app_endpoints")
#     rows = cursor.fetchall()
    
#     conn.close()
    
#     return rows

# def build_dict_of_dicts(rows):
#     data_dict = {}
    
#     for path, dep_list in rows:
#         try:
#             dependencies = eval(dep_list)  
#             if isinstance(dependencies, list):
#                 data_dict[path] = [dep.strip() for dep in dependencies if dep.strip()]
#         except:
#             print(f"Failed to parse dependencies for {path}: {dep_list}")
    
#     return data_dict

# def build_tree_from_dict(data_dict):
#     nodes = {key: TreeNode(key) for key in data_dict.keys()}
#     processed_paths = set()
#     for key, children in data_dict.items():
#         if key in nodes:
#             node = nodes[key]
#             for child_key in children:
#                 if child_key in nodes:
#                     child_node = nodes[child_key]
#                     node.add_child(child_node)
#             processed_paths.add(key)
    
#     root_nodes = [node for key, node in nodes.items() if key not in processed_paths]
    

#     if not root_nodes:
#         remaining_nodes = [node for key, node in nodes.items()]
#         root_nodes = remaining_nodes
    
#     return root_nodes

# def print_tree(node, level=0):
#     indent = " " * (level * 2)
#     print(f"{indent}{node.value}")
#     for child in node.children:
#         print_tree(child, level + 1)


# if __name__ == "__main__":

#     db_path = 'db.sqlite3'
    

#     rows = fetch_data_from_db(db_path)
#     print("Fetched rows:", rows)
    

#     data_dict = build_dict_of_dicts(rows)
    

#     root_nodes = build_tree_from_dict(data_dict)
    

#     if root_nodes:
#         for root in root_nodes:
#             print_tree(root)
#     else:
#         print('No Tree Found')
    
# ***************************************************************************
# ***************************************************************************
# import sqlite3
# import sys

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1000)

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

#     def add_child(self, child_node):
#         self.children.append(child_node)

#     def __repr__(self):
#         return f"TreeNode({self.value})"

# def fetch_data_from_db(db_path):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
    
#     # Fetch all rows from the table
#     cursor.execute("SELECT path, dependency_list FROM dependency_app_endpoints")
#     rows = cursor.fetchall()
    
#     conn.close()
    
#     return rows

# def build_dict_of_dicts(rows):
#     data_dict = {}
    
#     for path, dep_list in rows:
#         try:
#             dependencies = eval(dep_list)  
#             if isinstance(dependencies, list):
#                 data_dict[path] = [dep.strip() for dep in dependencies if dep.strip()]
#         except:
#             print(f"Failed to parse dependencies for {path}: {dep_list}")
    
#     return data_dict

# def build_tree_from_dict(data_dict):
#     nodes = {key: TreeNode(key) for key in data_dict.keys()}
#     visited = set()
#     recursion_stack = set()

#     def dfs(current_node):
#         if current_node in recursion_stack:
#             # Create a special indicator for cycles
#             cycle_node = TreeNode(f"Cycle detected: {current_node}")
#             nodes[current_node].add_child(cycle_node)
#             return

#         if current_node in visited:
#             return

#         visited.add(current_node)
#         recursion_stack.add(current_node)

#         node = nodes[current_node]
#         for child_key in data_dict.get(current_node, []):
#             if child_key in nodes:
#                 dfs(child_key)
#                 child_node = nodes[child_key]
#                 node.add_child(child_node)
        
#         recursion_stack.remove(current_node)

#     for key in data_dict.keys():
#         if key not in visited:
#             dfs(key)

#     return nodes

# # Example usage:
# db_path = 'db.sqlite3'
# rows = fetch_data_from_db(db_path)
# data_dict = build_dict_of_dicts(rows)
# nodes = build_tree_from_dict(data_dict)

# # Output the tree structure
# for key, node in nodes.items():
#     print(f"Node: {node.value}")
#     for child in node.children:
#         print(f"  -> Child: {child.value}")

# *****************************************************************************
# *****************************************************************************

# import sqlite3
# import sys
# import networkx as nx
# import matplotlib.pyplot as plt

# # Increase recursion limit if necessary
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1000)

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []
#         self.is_cycle = False  # Indicates if this node is part of a cycle

#     def add_child(self, child_node):
#         self.children.append(child_node)

#     def __repr__(self):
#         return f"TreeNode({self.value}, is_cycle={self.is_cycle})"

# def fetch_data_from_db(db_path):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
    
#     # Fetch all rows from the table
#     cursor.execute("SELECT path, dependency_list FROM dependency_app_endpoints")
#     rows = cursor.fetchall()
    
#     conn.close()
#     return rows

# def build_dict_of_dicts(rows):
#     data_dict = {}
#     for path, dep_list in rows:
#         try:
#             dependencies = eval(dep_list)
#             if isinstance(dependencies, list):
#                 data_dict[path] = [dep.strip() for dep in dependencies if dep.strip()]
#         except:
#             print(f"Failed to parse dependencies for {path}: {dep_list}")
#     return data_dict

# def build_tree_from_dict(data_dict):
#     nodes = {key: TreeNode(key) for key in data_dict.keys()}
#     visited = set()
#     recursion_stack = set()

#     def dfs(current_node):
#         if current_node in recursion_stack:
#             # Mark the current node as a cycle node
#             cycle_node = TreeNode(f"Cycle detected: {current_node}")
#             cycle_node.is_cycle = True
#             nodes[current_node].add_child(cycle_node)
#             return

#         if current_node in visited:
#             return

#         visited.add(current_node)
#         recursion_stack.add(current_node)

#         node = nodes[current_node]
#         for child_key in data_dict.get(current_node, []):
#             if child_key in nodes:
#                 if child_key in recursion_stack:
#                     # Handle the cycle case
#                     cycle_node = nodes[child_key]
#                     cycle_node.is_cycle = True
#                     node.add_child(cycle_node)
#                 else:
#                     dfs(child_key)
#                     child_node = nodes[child_key]
#                     node.add_child(child_node)
        
#         recursion_stack.remove(current_node)

#     for key in data_dict.keys():
#         if key not in visited:
#             dfs(key)

#     return nodes

# def build_graph_from_tree(nodes):
#     G = nx.DiGraph()
#     def add_edges(node):
#         for child in node.children:
#             if not child.is_cycle:
#                 G.add_edge(node.value, child.value)
#                 add_edges(child)
#             else:
#                 G.add_edge(node.value, f"Cycle: {child.value}")

#     for node in nodes.values():
#         add_edges(node)
#     return G

# def visualize_graph(G):
#     plt.figure(figsize=(15, 12))
#     pos = nx.spring_layout(G, seed=42)
#     nx.draw(G, pos, with_labels=True, arrows=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
#     plt.title("Dependency Tree with Cycles Representation")
#     plt.show()

# db_path = 'db.sqlite3'  
# rows = fetch_data_from_db(db_path)
# data_dict = build_dict_of_dicts(rows)
# nodes = build_tree_from_dict(data_dict)
# G = build_graph_from_tree(nodes)
# visualize_graph(G)


# ******************************************************************************************************
# ******************************************************************************************************

import json

class TreeNode:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children if children is not None else []

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.name) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

def build_tree_from_json(json_data):
    def build_node(name, children_data):
        children = [build_node(child_name, child_data) for child_name, child_data in children_data.items()]
        return TreeNode(name, children)
    
    # The root of the tree
    root_name = list(json_data.keys())[0]
    root_children_data = json_data[root_name]["children"]
    return build_node(root_name, root_children_data)

# Sample JSON data
json_str = '''
{
  "/": {
    "children": {
      "/rest/admin/application-configuration": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/socket.io/": {},
      "/rest/admin/application-version": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/api/Challenges/": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/languages": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/api/Quantitys/": {
        "children": {
          "/api/Complaints/": {},
          "/api/Challenges/": {},
          "/rest/products/search": {},
          "/api/Cards/": {},
          "/api/Feedbacks/": {},
          "/api/Addresss/": {},
          "/rest/saveLoginIp": {},
          "/api/Cards": {}
        }
      },
      "/rest/products/search": {
        "children": {
          "/api/Complaints/": {},
          "/api/Challenges/": {},
          "/api/Cards/": {},
          "/api/Feedbacks/": {},
          "/api/Quantitys/": {},
          "/api/Addresss/": {},
          "/rest/saveLoginIp": {},
          "/api/Cards": {}
        }
      },
      "/font-mfizz.woff": {},
      "/assets/public/favicon_js.ico": {},
      "/api/SecurityQuestions/": {},
      "/api/Users/": {},
      "/api/SecurityAnswers/": {},
      "/rest/user/whoami": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/user/": {},
      "/rest/basket/6": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/1/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/24/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/6/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/30/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/3/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/25/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/api/BasketItems/": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/22": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/22/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/1": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/24": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/6": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/30": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/3": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/25": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/41/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/41": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/39/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/40/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/40": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/27/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/5/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/5": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/33/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/38/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/33": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/8/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/8": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/34/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/37/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/19": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/19/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/13": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/13/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/26/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/14": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/14/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/18": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      },
      "/rest/products/18/reviews": {
        "children": {
          "/api/Users/": {},
          "/rest/products/reviews": {},
          "/rest/user/": {}
        }
      },
      "/api/Products/15": {
        "children": {
          "/api/Users/": {},
          "/rest/user/": {}
        }
      }
    }
  }
}

'''

# Parse JSON
json_data = json.loads(json_str)

# Build tree
root = build_tree_from_json(json_data)

# Print tree
print(root)


