# # import json
# # from haralyzer import HarParser

# # def parse_har_file(har_file_path):
# #     with open(har_file_path, 'r', encoding='utf-8') as f:
# #         har_data = json.loads(f.read())
# #         har_parser = HarParser(har_data)
# #         # Debugging: Print the keys of the parsed HAR data
# #         print(har_parser.har_data.keys())
# #     return har_parser.har_data['entries']


# # def extract_params_from_response(response):
# #     try:
# #         response_content = json.loads(response['content']['text'])
# #         if 'data' in response_content:
# #             return response_content['data'].keys()
# #     except:
# #         return []

# # def extract_params_from_request(request):
# #     try:
# #         request_content = json.loads(request['postData']['text'])
# #         return request_content.keys()
# #     except:
# #         return []


# # def find_dependencies(har_entries):
# #     api_responses = {}
# #     api_requests = {}

# #     for entry in har_entries:
# #         request = entry['request']
# #         response = entry['response']
# #         url = request['url']
        
# #         request_params = extract_params_from_request(request)
# #         print('request')
# #         print('-'*80)
# #         print(url)
# #         print('-'*80)
# #         if request_params is not None:
# #             print(request_params)
# #         print('-'*80)
# #         response_params = extract_params_from_response(response)
# #         print('response')
# #         print('-'*80)
# #         print(url)
# #         print('-'*80)
# #         if response_params is not None:
# #             print(response_params)
# #         print('-'*80)
        
# #         api_responses[url] = response_params
# #         api_requests[url] = request_params
    
# #     dependency_list = {}

# #     # for api,req_params in api_requests.items():
# #     #     print(f"{api}---->{req_params}")
    
# #     # for apii,response_params in api_responses.items():
# #     #             print("response")
# #     #             print(f"{apii}---->{response_params}")
            
# #     # print(api_requests.items())
    
# #     # if api_requests.items() is not None:
# #     #     for api, req_params in api_requests.items():  
            
# #     #         # print(f"{api}--->{req_params}") 
# #     #         dependencies = []
# #     #         if api_responses.items() is not None:
                
# #     #             for res_url, res_params in api_responses.items():
# #     #                 if (res_params is not None):
# #     #                     if(any(param in res_params for param in req_params)):
# #     #                         dependencies.append(res_url)
                
# #     #             for req_url, req_other_params in api_requests.items():
# #     #                 if req_url != api and any(param in req_other_params for param in req_params):
# #     #                     dependencies.append(req_url)
    
            
    
    
# #     #         # dependency_list[api] =dependencies
# #     #         dependency_list[api] = dependencies 
# #     # dependency_list = {}

# #     for api, req_params in api_requests.items():
# #         dependencies = []
# #         for req_url, req_other_params in api_requests.items():
# #             if req_url != api and any(param in req_other_params for param in req_params) :
# #                 dependencies.append(req_url)
# #         for res_url, res_params in api_responses.items():
# #             if res_params and any(param in res_params for param in req_params):
# #                 dependencies.append(res_url)
        
        

# #         dependency_list[api] = dependencies
        
    
# #     # if api_requests.items() is not None:
# #     #     for api,request_params in api_requests.items():
# #     #         dependencies = []
# #     #         if api_requests.items() is not None:
# #     #             for req_url,req_params in api_responses.items():
# #     #                 if(req_params is not None):
# #     #                     if(any(param in req_params for param in req_params)):
# #     #                         dependencies.append(req_url)
# #     #         dependency_list[api] =dependencies 

# #     return dependency_list


# # def map_dependencies(dependency_list):
# #     dependency_map = {}

# #     for url, dependencies in dependency_list.items():
# #         dependency_map[url] = dependencies

# #     return dependency_map



# # def main(har_file_path):
# #     har_entries = parse_har_file(har_file_path)
# #     dependency_list = find_dependencies(har_entries)
    
# #     # for url, dependencies in dependency_list.items():
# #     #     print(f"url: {url}")
# #     #     print(f"dependency: {dependencies}")
# #     #     print("-" * 80)
# #         # request_entry = (entry for entry in har_entries if entry['request']['url']==url)
# #     #     # response_entry = 
    
        

# #     dependency_map = map_dependencies(dependency_list)
# #     # print(dependency_map)
# #     for url, deps in dependency_map.items():
# #         if len(deps) is not 0:
# #             print(f"{url}: {deps}")
    

# # har_file_path = 'youtube.har'
# # main(har_file_path)


# import json
# from haralyzer import HarParser
# from urllib.parse import urlparse, parse_qs, urlunparse

# # Helper function to extract keys from nested dictionaries
# def extract_keys(obj, prefix=''):
#     keys = []
#     if isinstance(obj, dict):
#         for k, v in obj.items():
#             full_key = f"{prefix}.{k}" if prefix else k
#             keys.append(full_key)
#             keys.extend(extract_keys(v, full_key))
#     elif isinstance(obj, list):
#         for i, item in enumerate(obj):
#             full_key = f"{prefix}[{i}]"
#             keys.append(full_key)
#             keys.extend(extract_keys(item, full_key))
#     return keys

# # def parse_har_file(har_file_path):
# #     with open(har_file_path, 'r', encoding='utf-8') as f:
# #         har_data = json.loads(f.read())
# #         har_parser = HarParser(har_data)
# #         # Debugging: Print the keys of the parsed HAR data
# #         print(har_parser.har_data.keys())
# #     return har_parser.har_data['log']['entries']

# def parse_har_file(har_file_path):
#     with open(har_file_path, 'r', encoding='utf-8') as f:
#         har_data = json.loads(f.read())
#         har_parser = HarParser(har_data)
#         # Debugging: Print the keys of the parsed HAR data
#         print(har_parser.har_data.keys())
#     return har_parser.har_data['entries']

# def extract_params_from_response(response):
#     try:
#         response_content = json.loads(response['content']['text'])
#         if 'data' in response_content:
#             return extract_keys(response_content['data'])
#     except:
#         return []
#     return []

# def extract_params_from_request(request):
#     try:
#         request_content = json.loads(request['postData']['text'])
#         return extract_keys(request_content)
#     except:
#         return []
#     return []

# def find_dependencies(har_entries):
#     api_responses = {}
#     api_requests = {}

#     for entry in har_entries:
#         request = entry['request']
#         response = entry['response']
#         url = request['url']
        
#         request_params = extract_params_from_request(request)
#         response_params = extract_params_from_response(response)
        
#         api_responses[url] = response_params
#         api_requests[url] = request_params
    
#     dependency_list = {}

#     for api, req_params in api_requests.items():
#         dependencies = []
        
#         # Cross-reference with other responses
#         for res_url, res_params in api_responses.items():
#             if res_params and any(param in res_params for param in req_params):
#                 dependencies.append(res_url)
        
#         # Cross-reference with other requests
#         for req_url, req_other_params in api_requests.items():
#             if req_url != api and any(param in req_other_params for param in req_params):
#                 dependencies.append(req_url)
        
#         dependency_list[api] = dependencies

#     return dependency_list

# def get_paths_from_url(url):
#     parsed_url = urlparse(url)
#     base_path = parsed_url.path
#     query_params = parse_qs(parsed_url.query)
#     return base_path, query_params

# def extract_resembling_paths(har_entries, base_path):
#     resembling_paths = []
#     for entry in har_entries:
#         entry_url = entry['request']['url']
#         entry_path, _ = get_paths_from_url(entry_url)
#         if entry_path.startswith(base_path):
#             resembling_paths.append(entry_url)
#     return resembling_paths

# def map_dependencies(dependency_list, har_entries):
#     dependency_map = {}

#     for url, dependencies in dependency_list.items():
#         base_path, query_params = get_paths_from_url(url)
#         resembling_paths = extract_resembling_paths(har_entries, base_path)
        
#         dependency_map[url] = {
#             'dependencies': dependencies,
#             'resembling_paths': resembling_paths
#         }

#     return dependency_map

# def main(har_file_path):
#     har_entries = parse_har_file('Juiceshop1.har')
#     dependency_list = find_dependencies(har_entries)

#     for url, dependencies in dependency_list.items():
#         print(f"URL: {url}")
#         print(f"Dependencies: {dependencies}")
#         print("-" * 80)
#         # request = ''
        
#         request_entry = (entry for entry in har_entries if entry['request']['url']==url)
#         response_entry = (entry for entry in har_entries if entry['response']['url']==url)
#         for entry in har_entries:
#             request = entry['request']
#             response = entry['response']
#         if request_entry:
#             request_params = extract_params_from_request(request)
#             print(f"Request Parameters: {request_params}")
        
#         if response_entry:
#             response_params = extract_params_from_response(response)
#             print(f"Response Parameters: {response_params}")
        
#         print("-" * 80)
    
#     dependency_map = map_dependencies(dependency_list, har_entries)
    
#     # Print the dependency map with resembling paths
#     print("Dependency Map:")
#     for url, details in dependency_map.items():
#         print(f"{url}:")
#         print(f"  Dependencies: {details['dependencies']}")
#         print(f"  Resembling Paths: {details['resembling_paths']}")

# har_file_path = 'Juiceshop1.har'
# main(har_file_path)
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



# from urllib.parse import urlparse

# from urllib.parse import urlparse

# x = ord("h")
# print(x)

import json
import rest_framework
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileUploadSerializer
from .models import HarFile, Endpoints
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from urllib.parse import urlparse

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
            for page in pages:
                base_path = page['title']

            api_responses = {}
            api_requests = {}
            path_trie = Trie()
            dependency_list = {}
            auth_related_endpoints = []

            for entry in entries:
                request_info = entry['request']
                response_info = entry['response']
                method = request_info['method']

                cookies = request_info['cookies']
                full_url = request_info['url']
                parsed_url = urlparse(full_url)
                base_path = f"{parsed_url.scheme}://{parsed_url.netloc}"
                path = parsed_url.path

                path_trie.insert(path)

                query_params = request_info.get('queryString', [])
                response_status = response_info['status']

                headers = request_info.get('headers', [])
                response_headers = response_info.get('headers', [])
                response_body = json.dumps(response_info.get('content', []))

                request_parameters = request_info.get('postData', {}).get('text', {})
                response_parameters = response_info.get('content', {}).get('text', {})

                try:
                    request_parameters3 = json.loads(request_parameters) if isinstance(request_parameters, str) else request_parameters
                    request_parameters3 = list(request_parameters3.keys()) if isinstance(request_parameters3, dict) else request_parameters3
                except json.JSONDecodeError:
                    request_parameters3 = {}

                try:
                    response_parameters3 = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
                    if isinstance(response_parameters3, dict):
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
                        response_parameters3 = list(response_parameters3.keys()) + list(data_keys)
                    else:
                        response_parameters3 = list(response_parameters3) if isinstance(response_parameters3, list) else response_parameters3
                except json.JSONDecodeError:
                    response_parameters3 = {}

                if not isinstance(request_parameters3, list):
                    request_parameters3 = list(request_parameters3)

                if query_params:
                    query_param_keys = [param['name'] for param in query_params]
                    request_parameters3.extend(query_param_keys)
                
                # Remove 'status' and 'data' from response parameters
                response_parameters3 = [param for param in response_parameters3 if param not in ['status', 'data']]

                token_headers = {}
                non_token_headers = {}

                referrer = ''
                dependencies = []
                if 'email' in request_parameters3 and 'password' in request_parameters3:
                    auth_related_endpoints.append(path)

                for header in headers:
                    header_name = header.get('name', '').lower()
                    header_value = header.get('value', '')
                    if 'token' in header_name or header_name == 'authorization':
                        token_headers[header_name] = header_value
                        authentication = header_value
                        for dash in auth_related_endpoints:
                            dependencies.append(dash)
                    elif header_name == 'referer' or header_name == 'referrer':
                        referrer = header_value
                    else:
                        non_token_headers[header_name] = header_value

                # Identify login endpoint (with 'email' and 'password')
                

                requires_token = any('token' in header for header in token_headers)

                # Dependency logic
                for req_url, req_other_params in api_requests.items():
                    if req_url != path and any(param in req_other_params for param in request_parameters3):
                        dependencies.append(req_url)
                for res_url, res_params in api_responses.items():
                    if res_params and any(param in res_params for param in request_parameters3):
                        if res_url not in dependencies:
                            dependencies.append(res_url)
                if referrer and referrer not in dependencies:
                    dependencies.append(referrer)

                # Adding pattern matching dependencies using Trie
                similar_paths = path_trie.search_similar_paths(path)
                for similar_path in similar_paths:
                    if similar_path != path and similar_path not in dependencies:
                        dependencies.append(similar_path)

                
                        

                if isinstance(path, str):
                    dependency_list[path] = dependencies
                
                # print(auth_related_endpoints)
                Endpoints.objects.create(
                    base_path=base_path,
                    path=path,
                    method=method,
                    query_params=query_params,
                    requestBody=request_info,
                    headers=headers,
                    response_parameters=response_parameters3,
                    request_parameters=request_parameters3,
                    responses={'status': response_status},
                    responsebody=json.loads(response_body),
                    response_header=response_headers,
                    authentication=token_headers.get('authorization', {}),
                    referrer=referrer,
                    dependency_list=list(set(dependency_list.get(path, [])))
                )

            return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)
