# import json
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import FileUploadSerializer
# from .models import HarFile, Endpoints
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
# from urllib.parse import urlparse
# import os
# from django.views import View
# from django.shortcuts import render
# from django.http import HttpResponse
# from graphviz import Digraph
# from collections import defaultdict
# import re
# from datetime import datetime

# def extract_login_from_url(url):
#     match = re.search(r'login', url, re.IGNORECASE)
#     if match:
#         return match.group(0)
#     return None

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_path = False
#         self.paths = []

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, path):
#         node = self.root
#         segments = path.strip('/').split('/')
#         for segment in segments:
#             if segment not in node.children:
#                 node.children[segment] = TrieNode()
#             node = node.children[segment]
#         node.is_end_of_path = True
#         node.paths.append(path)

#     def search_similar_paths(self, path):
#         node = self.root
#         segments = path.strip('/').split('/')
#         similar_paths = set()

#         def dfs(current_node, current_segments):
#             if current_node.is_end_of_path:
#                 similar_paths.update(current_node.paths)
#             for segment, child_node in current_node.children.items():
#                 if segment in current_segments:
#                     dfs(child_node, current_segments)

#         dfs(node, segments)
#         return list(similar_paths)

# class UploadHarFile(APIView):
#     queryset = HarFile.objects.all()
#     serializer_class = FileUploadSerializer
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, *args, **kwargs):
#         file_obj = request.data.get('file_upload')
#         if not file_obj:
#             return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             file_name = file_obj.name
#             if not file_name.endswith('.har'):
#                 return Response({'error': 'Unsupported file format.'}, status=status.HTTP_400_BAD_REQUEST)

#             har_content = json.load(file_obj)

#             if 'log' not in har_content or 'entries' not in har_content['log']:
#                 return Response({'error': 'Invalid HAR file format.'}, status=status.HTTP_400_BAD_REQUEST)

#             entries = har_content['log']['entries']
#             pages = har_content['log']['pages']
#             sorted_entries = sorted(entries, key=lambda x: x['startedDateTime'])

            
#             for page in pages:
#                 base_path = page['title']
#             login_endpoint_found =False
#             login_endpoint_index = -1
#             for i, entry in enumerate(sorted_entries):
#                 request_info = entry['request']
#                 full_url = request_info['url']
#                 if extract_login_from_url(full_url):
#                     login_endpoint_found = True
#                     login_endpoint_index = i
#                     break

#             # if not login_endpoint_found:
#             #     return Response({'error': 'No login endpoint found in HAR file.'}, status=status.HTTP_400_BAD_REQUEST)
            
#             filtered_entries = sorted_entries[login_endpoint_index:]
#             api_responses = {}
#             api_requests = {}
#             path_trie = Trie()
#             dependency_list = {}
#             auth_related_endpoints = []
#             login_endpoints = None
            
#             def generalize_path(path):
#                 segments = path.strip('/').split('/')
#                 generalized_segments = [segment if not segment.isdigit() else '{id}' for segment in segments]
#                 return '/'.join(generalized_segments)
#             for entry in filtered_entries:
#                 request_info = entry['request']
#                 response_info = entry['response']
#                 method = request_info['method']
#                 start_date_time = entry.get('startedDateTime', '')
#                 cookies = request_info['cookies']
#                 full_url = request_info['url']
#                 parsed_url = urlparse(full_url)
#                 base_path = f"{parsed_url.scheme}://{parsed_url.netloc}"
#                 path = parsed_url.path
#                 if any(ext in path for ext in ['.jpg', '.min.css', '.js','.jpeg','.png','css','woff2','svg','ico','.woff']):
#                     continue

#                 path_trie.insert(path)

#                 query_params = request_info.get('queryString', [])
#                 response_status = response_info['status']

#                 headers = request_info.get('headers', [])
#                 response_headers = response_info.get('headers', [])
#                 response_body = json.dumps(response_info.get('content', []))

#                 request_parameters = request_info.get('postData', {}).get('text', {})
#                 response_parameters = response_info.get('content', {}).get('text', {})

#                 try:
#                     request_parameters3 = json.loads(request_parameters) if isinstance(request_parameters, str) else request_parameters
#                     request_parameters3 = list(request_parameters3.keys()) if isinstance(request_parameters3, dict) else request_parameters3
#                 except json.JSONDecodeError:
#                     request_parameters3 = {}

#                 try:
#                     response_parameters3 = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
#                     if isinstance(response_parameters3, list):
#                         # Check if the list contains dictionaries
#                         if all(isinstance(item, dict) for item in response_parameters3):
#                             keys = set()
#                             for item in response_parameters3:
#                                 keys.update(item.keys())
#                             response_parameters3 = list(keys)
#                         else:
#                             response_parameters3 = list(response_parameters3)
#                     elif isinstance(response_parameters3, dict):
#                         data_keys = []
#                         if 'data' in response_parameters3:
#                             if isinstance(response_parameters3['data'], str):
#                                 try:
#                                     response_parameters3['data'] = json.loads(response_parameters3['data'])
#                                 except json.JSONDecodeError:
#                                     response_parameters3['data'] = {}
#                             if isinstance(response_parameters3['data'], dict):
#                                 data_keys = response_parameters3['data'].keys()
#                             elif isinstance(response_parameters3['data'], list) and len(response_parameters3['data']) > 0:
#                                 if isinstance(response_parameters3['data'][0], dict):
#                                     data_keys = response_parameters3['data'][0].keys()
#                                 else:
#                                     data_keys = []
#                             else:
#                                 data_keys = []
#                         response_parameters3 = list(response_parameters3.keys()) + list(data_keys)
#                     else:
#                         response_parameters3 = list(response_parameters3) if isinstance(response_parameters3, list) else response_parameters3
#                 except json.JSONDecodeError:
#                     response_parameters3 = {}

#                 if not isinstance(request_parameters3, list):
#                     request_parameters3 = list(request_parameters3)

#                 if query_params:
#                     query_param_keys = [param['name'] for param in query_params]
#                     request_parameters3.extend(query_param_keys)
                
#                 # Remove 'status' and 'data' from response parameters
#                 response_parameters3 = [param for param in response_parameters3 if param not in ['status', 'data']]
                
#                 #logic for producer apis
#                 is_producer = False
#                 if method=='POST' and response_status==201:
#                     is_producer = True
                
                
#                 if extract_login_from_url(base_path):
#                     login_endpoints = base_path
                

#                 token_headers = {}
#                 non_token_headers = {}

#                 referrer = ''
#                 authentication = {}
#                 dependencies = []
#                 if 'email' in request_parameters3 and 'password' in request_parameters3:
#                     auth_related_endpoints.append(path)

#                 for header in headers:
#                     header_name = header.get('name', '').lower()
#                     header_value = header.get('value', '')
#                     if 'token' in header_name or header_name == 'authorization':
#                         token_headers[header_name] = header_value
#                         authentication = header_value
#                         for dash in auth_related_endpoints:
#                             dependencies.append(dash)
#                     elif header_name == 'cookie':
#                         cookies = header_value.split('; ')
#                         for cookie in cookies:
#                             if cookie.startswith('token='):
#                                 token_value = cookie.split('=')[1]
#                                 token_headers['cookie'] = token_value
#                                 authentication = token_value
#                                 for dash in auth_related_endpoints:
#                                     dependencies.append(dash)
#                     elif header_name == 'referer' or header_name == 'referrer':
#                         referrer = header_value
#                     else:
#                         non_token_headers[header_name] = header_value
                
                

                
#                 api_requests[path] = request_parameters3
#                 api_responses[path] = response_parameters3

#                 #searching in response parameters across all
#                 for req_url, req_other_params in api_responses.items():
#                     if req_url != path and (any(param in req_other_params for param in request_parameters3)
#                                             or
#                                             any(param in req_other_params for param in response_parameters3)):
#                         dependencies.append(req_url)
                
#                 # searching in request parameters across all other than the current path
#                 for req_url, req_other_params in api_requests.items():
#                     if req_url != path and (any(param in req_other_params for param in request_parameters3)
#                                             or
#                                             any(param in req_other_params for param in response_parameters3)):
#                         dependencies.append(req_url)

#                 # if referrer and referrer not in dependencies:
#                 #     dependencies.append(referrer)

                
#                 similar_paths = path_trie.search_similar_paths(path)
#                 for similar_path in similar_paths:
#                     if similar_path != path and similar_path not in dependencies:
#                         dependencies.append(similar_path)
                
#                 generalized_path = generalize_path(path)
#                 if generalized_path not in dependency_list:
#                     dependency_list[generalized_path] = set()
#                 dependency_list[generalized_path].update(dependencies)

#                 if isinstance(path, str):
#                     dependency_list[path] = dependencies
                
#                 # if request_parameters3 or response_parameters3:
#                     Endpoints.objects.create(
#                         base_path=base_path,
#                         path=path,
#                         method=method,
#                         query_params=query_params,
#                         requestBody=request_info,
#                         headers=headers,
#                         response_parameters=response_parameters3,
#                         request_parameters=request_parameters3,
#                         responses={'status': response_status},
#                         is_producer_api = is_producer,
#                         responsebody=json.loads(response_body),
#                         response_header=response_headers,
#                         authentication=authentication,
#                         referrer=referrer,
#                         dependency_list=list(set(dependency_list.get(path, []))),
#                         login_endpoint = login_endpoints,
#                         start_date_time=datetime.strptime(start_date_time, '%Y-%m-%dT%H:%M:%S.%fZ')  # Save the start date time
#                     )

#             return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)



#     def generalize_path(self, path):
#         segments = path.strip('/').split('/')
#         generalized_segments = []
        
#         is_in_numeric_segment = False
        
#         for segment in segments:
#             if segment.isdigit():
#                 if not is_in_numeric_segment:
#                     generalized_segments.append('{id}')
#                     is_in_numeric_segment = True
#                 else:
#                     generalized_segments.append(segment)
#             else:
#                 generalized_segments.append(segment)
        
#         return '/'.join(generalized_segments)
    




# # Function to generalize paths with IDs
# def generalize_path(path):
#     generalized_path = []
#     for part in path.split('/'):
#         if part.isdigit():
#             generalized_path.append('{id}')
#         else:
#             generalized_path.append(part)
#     return '/'.join(generalized_path)

# # Function to build the execution flow and dependency tree
# def build_execution_flow(endpoints):
#     tree = defaultdict(dict)
#     execution_flow = []
#     visited = set()

#     def process_path(path, dependencies):
#         generalized_path = generalize_path(path)
#         if '{id}' in generalized_path or generalized_path in visited:
#             return
#         visited.add(generalized_path)
#         refined_dependencies = []
#         for dep in dependencies:
#             generalized_dep = generalize_path(dep)
#             if '{id}' not in generalized_dep and generalized_dep not in visited:
#                 tree[generalized_path][generalized_dep] = {}
#                 refined_dependencies.append(generalized_dep)
#         execution_flow.append((generalized_path, refined_dependencies))

#     for path, dependencies in endpoints.items():
#         process_path(path, dependencies)

#     return tree, execution_flow


# def fetch_endpoints_data():
#     endpoints_data = {}
#     endpoints = Endpoints.objects.all()  
#     for endpoint in endpoints:
#         path = endpoint.path
#         dependencies = eval(endpoint.dependency_list)  
#         endpoints_data[path] = dependencies
#     return endpoints_data


# def visualize_execution_flow_with_dependencies(execution_flow):
#     dot = Digraph(comment='API Execution Flow with Dependencies')

#     for i, (current_node, dependencies) in enumerate(execution_flow):
#         dot.node(current_node, current_node)

#         if i > 0:
#             previous_node = execution_flow[i-1][0]
#             dot.edge(previous_node, current_node)
        
#         for dep in dependencies:
#             dot.node(dep, dep)
#             dot.edge(current_node, dep)

  
#     return dot.pipe(format='png')


# class ApiExecutionFlowView(View):
#     def get(self, request):
#         endpoints_data = fetch_endpoints_data()
#         dependency_tree, execution_flow = build_execution_flow(endpoints_data)
#         graph_image = visualize_execution_flow_with_dependencies(execution_flow)
#         return HttpResponse(graph_image, content_type='image/png')


from rest_framework.response import Response
from rest_framework import status
from .serializers import FileUploadSerializer
from .models import HarFile, Endpoints
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from urllib.parse import urlparse
import os
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from graphviz import Digraph
from collections import defaultdict
import re
from drf_yasg.utils import swagger_auto_schema
from datetime import datetime
from rest_framework import status
from django.core.files.storage import default_storage
import json
import graphviz
from django.conf import settings

def extract_login_from_url(url):
    match = re.search(r'login', url, re.IGNORECASE)
    if match:
        return match.group(0)
    return None

import json


def extract_all_keys(data):
       
    keys = set()
    if isinstance(data, dict):
        for key, value in data.items():
            keys.add(key)
            keys.update(extract_all_keys(value))
    elif isinstance(data, list):
        for item in data:
            keys.update(extract_all_keys(item))
    return keys

    
    



# def extract_keys_from_response(response_parameters):
#     try:
#         # Parse response parameters if it's a string
#         response_parameters3 = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
        
#         # Initialize empty lists for keys
#         data_keys = []
#         text_keys = []

#         if isinstance(response_parameters3, dict):
#             # Extract keys from 'data' field if present
#             if 'data' in response_parameters3:
#                 data_field = response_parameters3['data']
#                 if isinstance(data_field, str):
#                     try:
#                         data_field = json.loads(data_field)
#                     except json.JSONDecodeError:
#                         data_field = {}
#                 if isinstance(data_field, dict):
#                     data_keys = list(data_field.keys())
#                 elif isinstance(data_field, list) and len(data_field) > 0:
#                     if isinstance(data_field[0], dict):
#                         data_keys = list(data_field[0].keys())
                
#             # Extract keys from 'text' field if present
#             if 'text' in response_parameters3:
#                 try:
#                     text_data = json.loads(response_parameters3['text'])
#                     if isinstance(text_data, dict):
#                         text_keys = list(text_data.keys())
#                     elif isinstance(text_data, list) and len(text_data) > 0:
#                         if isinstance(text_data[0], dict):
#                             # Extract keys from the first dictionary in the list
#                             text_keys = list(text_data[0].keys())
#                 except json.JSONDecodeError:
#                     text_keys = []
                
#             # Combine original keys with 'data' and 'text' keys
#             response_parameters3 = list(response_parameters3.keys()) + list(data_keys) + list(text_keys)

#         else:
#             response_parameters3 = list(response_parameters3) if isinstance(response_parameters3, list) else []

#     except json.JSONDecodeError:
#         response_parameters3 = []

import json

def extract_keys_from_response_parameters(response_parameters):
    try:
        # Load JSON if response_parameters is a string
        response_parameters3 = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
        
        # Function to recursively extract keys from JSON data
        def extract_keys(data):
            keys = set()
            if isinstance(data, dict):
                for key, value in data.items():
                    keys.add(key)
                    keys.update(extract_keys(value))
            elif isinstance(data, list):
                for item in data:
                    keys.update(extract_keys(item))
            return keys

        data_keys = set()
        text_keys = set()

        if isinstance(response_parameters3, dict):
            if 'data' in response_parameters3:
                data_value = response_parameters3['data']
                if isinstance(data_value, str):
                    try:
                        data_value = json.loads(data_value)
                    except json.JSONDecodeError:
                        data_value = {}
                if isinstance(data_value, dict) or isinstance(data_value, list):
                    data_keys = extract_keys(data_value)
            
            if 'text' in response_parameters3:
                try:
                    text_data = json.loads(response_parameters3['text'])
                    text_keys = extract_keys(text_data)
                except json.JSONDecodeError:
                    pass

            # Combine keys from all sources
            all_keys = list(response_parameters3.keys()) + list(data_keys) + list(text_keys)
        else:
            all_keys = list(response_parameters3.keys())

    except json.JSONDecodeError:
        all_keys = []

    return all_keys









class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_path = False
        self.paths = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path):
        node = self.root
        segments = path.strip('/').split('/')
        for segment in segments:
            if segment not in node.children:
                node.children[segment] = TrieNode()
            node = node.children[segment]
        node.is_end_of_path = True
        node.paths.append(path)

    def search_similar_paths(self, path):
        node = self.root
        segments = path.strip('/').split('/')
        similar_paths = set()

        def dfs(current_node, current_segments):
            if current_node.is_end_of_path:
                similar_paths.update(current_node.paths)
            for segment, child_node in current_node.children.items():
                if segment in current_segments:
                    dfs(child_node, current_segments)

        dfs(node, segments)
        return list(similar_paths)

class APIExecutionTree:
    def __init__(self):
        self.tree = defaultdict(list)
        self.seen_paths = set()

    def add_dependency(self, parent, child):
        if child not in self.seen_paths:
            self.tree[parent].append(child)
            self.seen_paths.add(child)

    def build_tree(self, dependency_dict):
        for parent, children in dependency_dict.items():
            for child in children:
                self.add_dependency(parent, child)
                
    def get_tree(self):
        return self.tree
    




class UploadHarFile(APIView):
    queryset = HarFile.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        file_obj = request.data.get('file_upload')
        if not file_obj:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            file_name = file_obj.name
            if not file_name.endswith('.har'):
                return Response({'error': 'Unsupported file format.'}, status=status.HTTP_400_BAD_REQUEST)

            har_content = json.load(file_obj)

            if 'log' not in har_content or 'entries' not in har_content['log']:
                return Response({'error': 'Invalid HAR file format.'}, status=status.HTTP_400_BAD_REQUEST)

            entries = har_content['log']['entries']
            pages = har_content['log']['pages']

            if not entries:
                return Response({'error': 'No entries found in HAR file.'}, status=status.HTTP_400_BAD_REQUEST)

            # sorted_entries = sorted(entries, key=lambda x: x['startedDateTime'])
            sorted_entries = entries
            login_endpoint_found = False
            login_endpoint_index = -1

            # Identify the login endpoint and its index
            for i, entry in enumerate(entries):
                request_info = entry['request']
                full_url = request_info['url']
                if extract_login_from_url(full_url):
                    login_endpoint_found = True
                    login_endpoint_index = i
                    break

            # if not login_endpoint_found:
            #     return Response({'error': 'No login endpoint found in HAR file.'}, status=status.HTTP_400_BAD_REQUEST)

            # Filter entries to include only the login endpoint and those after it
            filtered_entries = sorted_entries[login_endpoint_index:]

            path_trie = Trie()
            dependency_list_sorted = {}
            dependency_list = {}
            auth_related_endpoints = []
            login_endpoints = None
            api_requests = {}
            api_responses = {}

            def generalize_path(path):
                segments = path.strip('/').split('/')
                generalized_segments = [segment if not segment.isdigit() else '{id}' for segment in segments]
                return '/'.join(generalized_segments)
             
            for entry in filtered_entries:
                request_info = entry['request']
                response_info = entry['response']
                method = request_info['method']
                start_date_time = entry['startedDateTime']
                cookies = request_info['cookies']
                full_url = request_info['url']
                
                parsed_url = urlparse(full_url)
                base_path = f"{parsed_url.scheme}://{parsed_url.netloc}"
                path = parsed_url.path
                if any(ext in path for ext in ['.jpg', '.min.css', '.js','.jpeg','.png','css','woff2','svg','ico','.woff']):
                    continue

                path_trie.insert(path)

                query_params = request_info.get('queryString', [])
                response_status = response_info['status']

                headers = request_info.get('headers', [])
                response_headers = response_info.get('headers', [])
                response_body = json.dumps(response_info.get('content', []))

                request_parameters = request_info.get('postData', {}).get('text', {})
                response_parameters = response_info.get('content', {}).get('text', {})
                data_keyss = set()
                text_keysss = []
                # response_parameters2 = json.dumps(request_parameters) if isinstance(response_parameters,str) else response_parameters
                # if isinstance(response_parameters2,dict):
                #     for ke,val in response_parameters2:
                #         if isinstance(val,list):
                #             if isinstance(val[0],dict):
                #                 for kee,vall in val[0]:
                #                     data_keyss = kee
                            
                try:
                    request_parameters3 = json.loads(request_parameters) if isinstance(request_parameters, str) else request_parameters
                    request_parameters3 = list(request_parameters3.keys()) if isinstance(request_parameters3, dict) else request_parameters3
                    # print(response_parameters)
                    # print('**************************')
                    # print(response_parameters3)
                    if isinstance(request_parameters3, dict):
                        if 'text' in request_parameters3 and isinstance(request_parameters3['text'], str):
                            try:
                                text_data = json.loads(request_parameters3['text'])
                                if isinstance(text_data, dict):
                                    text_keys = text_data.keys()
                                else:
                                    text_keys = []
                            except json.JSONDecodeError:
                                text_keys = []
                        else:
                            text_keys = []
                        request_parameters3 = list(request_parameters3.keys()) + list(text_keys)
                        # print(response_parameters)
                        # print(response_parameters3)
                except json.JSONDecodeError:
                    request_parameters3 = {}
                
                
                try:
                    response_parameters3 = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
                
                    
                    if isinstance(response_parameters3, dict):
                        for key,values in response_parameters3.items():
                            if isinstance(values,list):
                                if isinstance(values[0],dict):
                                    text_keysss = values[0].keys()
                         
                        # text_keys = []
                        data_keys = []
                        
                            
                        if 'data' in response_parameters3:
                            if isinstance(response_parameters3['data'], str):
                                try:
                                    response_parameters3['data'] = json.loads(response_parameters3['data'])
                                except json.JSONDecodeError:
                                    response_parameters3['data'] = {}
                            if isinstance(response_parameters3['data'], dict):
                                data_keys = response_parameters3['data'].keys()
                            elif isinstance(response_parameters3['data'], list) and len(response_parameters3['data']) > 0:
                                if isinstance(response_parameters3['data'][0], dict):
                                    data_keys = response_parameters3['data'][0].keys()
                                else:
                                    data_keys = []
                            else:
                                data_keys = []
                                response_parameters3 = list(response_parameters3.keys()) + list(data_keys) + list(text_keys)
                                print(response_parameters3)
                            
                        else:
                            response_parameters3 = list(response_parameters3.keys()) + list(data_keys)
                except json.JSONDecodeError:
                    response_parameters3 = {}

                if not isinstance(response_parameters, list):
                    response_parameters3 = list(response_parameters3)
                    
                if query_params:
                    query_param_keys = [param['name'] for param in query_params]
                    request_parameters3.extend(query_param_keys)
                # response_parameters3 = response_parameters3 + list(data_keyss)
                
                
                
                # Remove 'status' and 'data' from response parameters
                response_parameters3 = [param for param in response_parameters3 if param not in ['status', 'data','message']]
                
                #logic for producer apis
                is_producer = False
                if method=='POST' and response_status==201:
                    is_producer = True
                
                if extract_login_from_url(base_path):
                    login_endpoints = base_path
                token_headers = {}
                non_token_headers = {}
                
                referrer = ''
                authentication = {}
                dependencies = []
                if (('email' in request_parameters3 and 'password' in request_parameters3) or ('username' in request_parameters3 and 'password' in request_parameters3)) :
                    auth_related_endpoints.append(path)

                for header in headers:
                    header_name = header.get('name', '').lower()
                    header_value = header.get('value', '')
                    if 'token' in header_name or header_name == 'authorization':
                        token_headers[header_name] = header_value
                        authentication = header_value
                        for dash in auth_related_endpoints:
                            dependencies.append(dash)
                    elif header_name == 'cookie':
                        cookies = header_value.split('; ')
                        for cookie in cookies:
                            if cookie.startswith('token='):
                                token_value = cookie.split('=')[1]
                                token_headers['cookie'] = token_value
                                authentication = token_value
                                for dash in auth_related_endpoints:
                                    dependencies.append(dash)
                    elif header_name == 'referer' or header_name == 'referrer':
                        referrer = header_value
                    else:
                        non_token_headers[header_name] = header_value
                
                
                # response_parameters3 = list(response_parameters3) + list(text_keysss)
                response_parameters4 = (response_parameters3 + list(set(text_keysss)))
                api_requests[path] = request_parameters3
                api_responses[path] = response_parameters4

                #searching in response parameters across all
                for req_url, req_other_params in api_responses.items():
                    if req_url != path and (any(param in req_other_params for param in request_parameters3)
                                            or
                                            any(param in req_other_params for param in response_parameters4)):
                        dependencies.append(req_url)
                
                # searching in request parameters across all other than the current path
                for req_url, req_other_params in api_requests.items():
                    if req_url != path and (any(param in req_other_params for param in request_parameters3)
                                            or
                                            any(param in req_other_params for param in response_parameters4)):
                        dependencies.append(req_url)

                # if referrer and referrer not in dependencies:
                #     dependencies.append(referrer)

                
                similar_paths = path_trie.search_similar_paths(path)
                for similar_path in similar_paths:
                    if similar_path != path and similar_path not in dependencies:
                        dependencies.append(similar_path)
                
                generalized_path = generalize_path(path)
                if generalized_path not in dependency_list:
                    dependency_list[generalized_path] = set()
                dependency_list[generalized_path].update(dependencies)

                if isinstance(path, str):
                    dependency_list[path] = dependencies
                
                # response_parameters4 = (response_parameters4)
                
                print(text_keysss)
                Endpoints.objects.create(
                    base_path=base_path,
                    path=path,
                    method=method,
                    query_params=query_params,
                    requestBody=request_info,
                    headers=headers,
                    response_parameters=response_parameters4,
                    request_parameters=request_parameters3,
                    responses={'status': response_status},
                    is_producer_api=is_producer,
                    responsebody=json.loads(response_body),
                    response_header=response_headers,
                    authentication=authentication,
                    referrer=referrer,
                    # dependency_list_sorted=list(set(dependency_list_sorted.get(path, []))),
                    dependency_list = list(set(dependency_list.get(path, []))),
                    login_endpoint=login_endpoints,
                    # start_date_time=datetime.strptime(start_date_time, '%Y-%m-%dT%H:%M:%S.%fZ')  
                )
                

            return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Error processing file: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def generalize_path(self, path):
        segments = path.strip('/').split('/')
        generalized_segments = []
        
        is_in_numeric_segment = False
        
        for segment in segments:
            if segment.isdigit():
                if not is_in_numeric_segment:
                    generalized_segments.append('{id}')
                    is_in_numeric_segment = True
                else:
                    generalized_segments.append(segment)
            else:
                generalized_segments.append(segment)
        
        return '/'.join(generalized_segments)
    




# # Function to generalize paths with IDs
def generalize_path(path):
    generalized_path = []
    for part in path.split('/'):
        if part.isdigit():
            generalized_path.append('{id}')
        else:
            generalized_path.append(part)
    return '/'.join(generalized_path)



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





def fetch_endpoints_data():
    endpoints_data = {}
    login_endpoint = None
    login_endpoint = Endpoints.login_endpoint
    
    
    endpoints = Endpoints.objects.all()  
    
    for endpoint in endpoints:
        path = endpoint.path
        login_endpoint = endpoint.login_endpoint
        dependencies = eval(endpoint.dependency_list) if endpoint.dependency_list else []
        endpoints_data[path] = dependencies
    
        
    return endpoints_data


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
    
   
    
    file_path = os.path.join(settings.MEDIA_ROOT, 'execution_flow_MITM')
    dot.render(filename=file_path, format='png', cleanup=True)

    return file_path





class ApiExecutionFlowView(View):
    def get(self, request):
        endpoints_data = fetch_endpoints_data()
        dependency_tree, execution_flow = build_execution_flow(endpoints_data)
        graph_image = visualize_execution_flow_with_dependencies(execution_flow)
        return HttpResponse(graph_image, content_type='image/png')

