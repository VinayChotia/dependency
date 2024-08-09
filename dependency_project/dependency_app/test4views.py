# import json
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import *
# from .models import *
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser

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
#             for page in pages:
#                 base_path = page['title']

#             api_responses = {}
#             api_requests = {}
#             dependency_list = {}

#             for entry in entries:
#                 request_info = entry['request']
#                 response_info = entry['response']
#                 method = request_info['method']

#                 cookies = request_info['cookies']
#                 path = request_info['url']

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
#                     if isinstance(response_parameters3, dict) and 'data' in response_parameters3:
#                         data_keys = response_parameters3['data'].keys() if isinstance(response_parameters3['data'], dict) else []
#                         response_parameters3 = list(response_parameters3.keys()) + list(data_keys)
#                     else:
#                         response_parameters3 = list(response_parameters3.keys()) if isinstance(response_parameters3, dict) else response_parameters3
#                 except json.JSONDecodeError:
#                     response_parameters3 = {}

#                 token_headers = {}
#                 non_token_headers = {}

#                 referrer = ''
#                 dependency = []
#                 authentication = []

#                 for header in headers:
#                     header_name = header.get('name', '').lower()
#                     header_value = header.get('value', '')
#                     if 'token' in header_name or header_name == 'authorization':
#                         token_headers[header_name] = header_value
#                         authentication = header_value
#                     elif header_name == 'referer' or header_name == 'referrer':
#                         referrer = header_value
#                     elif 'token' in header_name or header_name == 'authorization':
#                         dependency.append('/login')
#                     else:
#                         non_token_headers[header_name] = header_value

#                 api_requests[path] = request_parameters3
#                 api_responses[path] = response_parameters3

#                 # Generate dependencies for each path
#                 dependencies = []
#                 for req_url, req_other_params in api_requests.items():
#                     if req_url != path and any(param in req_other_params for param in request_parameters3):
#                         dependencies.append(req_url)
#                 for res_url, res_params in api_responses.items():
#                     if res_params and any(param in res_params for param in request_parameters3):
#                         if res_url not in dependencies:
#                             dependencies.append(res_url)
#                 if referrer and referrer not in dependencies:
#                     dependencies.append(referrer)
                
#                 dependency_list[path] = dependencies
                 

#                 Endpoints.objects.create(
#                     base_path=base_path,
#                     path=path,
#                     method=method,
#                     query_params=query_params,
#                     requestBody=request_info,
#                     headers=headers,
#                     response_parameters=response_parameters3,
#                     request_parameters=request_parameters3,
#                     responses={'status': response_status},
#                     responsebody=json.loads(response_body),
#                     response_header=response_headers,
#                     authentication=token_headers.get('authorization', {}),
#                     referrer=referrer,
#                     dependency_list=dependency_list[path]
#                 )

#             return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)

# import json
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import *
# from .models import *
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser

# class UploadHarFile(APIView):
#     queryset = HarFile.objects.all()
#     serializer_class = FileUploadSerializer
#     parser_classes = [MultiPartParser, FormParser]

#     def find_dependencies(self, api_requests, api_responses, request_parameters, response_parameter, path, referrer):
#         dependencies = []

#         # Check for request parameter keys in other request parameters
#         for req_url, req_other_params in api_requests.items():
#             if req_url != path and any(param in req_other_params for param in request_parameters):
#                 dependencies.append(req_url)

#         # Check for response parameter keys in other response parameters
#         for res_url, res_params in api_responses.items():
#             if res_params and any(param in res_params for param in request_parameters):
#                 if res_url not in dependencies:
#                     dependencies.append(res_url)
        
#         # Check for response parameter in other request parameters
#         for req_url, req_other_params in api_requests.items():
#             if req_url != path and response_parameter in req_other_params:
#                 dependencies.append(req_url)

#         # Check for response parameter in other response parameters
#         for res_url, res_params in api_responses.items():
#             if res_params and response_parameter in res_params:
#                 if res_url not in dependencies:
#                     dependencies.append(res_url)
                    
#         # Check the referrer
#         if referrer and referrer not in dependencies:
#             dependencies.append(referrer)
        
#         return dependencies

#     def update_dependency_list(self, api_requests, api_responses, request_parameters, response_parameter, path, referrer, dependency_list):
#         dependencies = self.find_dependencies(api_requests, api_responses, request_parameters, response_parameter, path, referrer)
#         dependency_list[path] = dependencies

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
#             for page in pages:
#                 base_path = page['title']

#             api_responses = {}
#             api_requests = {}
#             dependency_list = {}

#             for entry in entries:
#                 request_info = entry['request']
#                 response_info = entry['response']
#                 method = request_info['method']

#                 cookies = request_info['cookies']
#                 path = request_info['url']

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
#                     if isinstance(response_parameters3, dict) and 'data' in response_parameters3:
#                         data_keys = response_parameters3['data'].keys() if isinstance(response_parameters3['data'], dict) else []
#                         response_parameters3 = list(response_parameters3.keys()) + list(data_keys)
#                     else:
#                         response_parameters3 = list(response_parameters3.keys()) if isinstance(response_parameters3, dict) else response_parameters3
#                 except json.JSONDecodeError:
#                     response_parameters3 = {}

#                 token_headers = {}
#                 non_token_headers = {}

#                 referrer = ''
#                 dependency = []
#                 authentication = []

#                 for header in headers:
#                     header_name = header.get('name', '').lower()
#                     header_value = header.get('value', '')
#                     if 'token' in header_name or header_name == 'authorization':
#                         token_headers[header_name] = header_value
#                         authentication = header_value
#                     elif header_name == 'referer' or header_name == 'referrer':
#                         referrer = header_value
#                     elif 'token' in header_name or header_name == 'authorization':
#                         dependency.append('/login')
#                     else:
#                         non_token_headers[header_name] = header_value

#                 api_requests[path] = request_parameters3
#                 api_responses[path] = response_parameters3

#                 self.update_dependency_list(api_requests, api_responses, request_parameters3, response_parameters3, path, referrer, dependency_list)

#                 Endpoints.objects.create(
#                     base_path=base_path,
#                     path=path,
#                     method=method,
#                     query_params=query_params,
#                     requestBody=request_info,
#                     headers=headers,
#                     response_parameters=response_parameters3,
#                     request_parameters=request_parameters3,
#                     responses={'status': response_status},
#                     responsebody=json.loads(response_body),
#                     response_header=response_headers,
#                     authentication=token_headers.get('authorization', {}),
#                     referrer=referrer,
#                     dependency_list=dependency_list[path]
#                 )

#             return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)

# import json
# import rest_framework
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import FileUploadSerializer
# from .models import HarFile, Endpoints
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
# from urllib.parse import urlparse

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
#             for page in pages:
#                 base_path = page['title']

#             api_responses = {}
#             api_requests = {}
#             path_trie = Trie()
#             dependency_list = {}
#             auth_related_endpoints = []

#             for entry in entries:
#                 request_info = entry['request']
#                 response_info = entry['response']
#                 method = request_info['method']

#                 cookies = request_info['cookies']
#                 full_url = request_info['url']
#                 parsed_url = urlparse(full_url)
#                 base_path = f"{parsed_url.scheme}://{parsed_url.netloc}"
#                 path = parsed_url.path

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
#                     if isinstance(response_parameters3, dict):
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

#                 token_headers = {}
#                 non_token_headers = {}

#                 referrer = ''
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
#                     elif header_name == 'referer' or header_name == 'referrer':
#                         referrer = header_value
#                     else:
#                         non_token_headers[header_name] = header_value

#                 # Identify login endpoint (with 'email' and 'password')
                

#                 requires_token = any('token' in header for header in token_headers)

#                 # Dependency logic
#                 for req_url, req_other_params in api_requests.items():
#                     if req_url != path and any(param in req_other_params for param in request_parameters3):
#                         dependencies.append(req_url)
#                 for res_url, res_params in api_responses.items():
#                     if res_params and any(param in res_params for param in request_parameters3):
#                         if res_url not in dependencies:
#                             dependencies.append(res_url)
#                 if referrer and referrer not in dependencies:
#                     dependencies.append(referrer)

#                 # Adding pattern matching dependencies using Trie
#                 similar_paths = path_trie.search_similar_paths(path)
#                 for similar_path in similar_paths:
#                     if similar_path != path and similar_path not in dependencies:
#                         dependencies.append(similar_path)

                
                        

#                 if isinstance(path, str):
#                     dependency_list[path] = dependencies
                
#                 # print(auth_related_endpoints)
#                 Endpoints.objects.create(
#                     base_path=base_path,
#                     path=path,
#                     method=method,
#                     query_params=query_params,
#                     requestBody=request_info,
#                     headers=headers,
#                     response_parameters=response_parameters3,
#                     request_parameters=request_parameters3,
#                     responses={'status': response_status},
#                     responsebody=json.loads(response_body),
#                     response_header=response_headers,
#                     authentication=token_headers.get('authorization', {}),
#                     referrer=referrer,
#                     dependency_list=list(set(dependency_list.get(path, [])))
#                 )

#             return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)
