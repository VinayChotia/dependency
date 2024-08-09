
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
#             for entry in entries:
#                 request_info = entry['request']
#                 response_info = entry['response']
#                 method = request_info['method']
                
                
#                 cookies = request_info['cookies']
#                 full_url = request_info['url']
#                 parsed_url = urlparse(full_url)
#                 base_path = f"{parsed_url.scheme}://{parsed_url.netloc}"
#                 path = parsed_url.path

                
#                 query_params = request_info.get('queryString', [])

#                 response_status = response_info['status']
                
#                 headers = request_info.get('headers', [])
#                 response_headers = response_info.get('headers', [])
#                 response_body = json.dumps(response_info.get('content', []))
                
                
                
                
#                 # request_parameters = (request_info.get('postData',{}))
#                 # request_parameters2 = request_parameters.get('text',{})
#                 # if type(request_parameters2)=='dict':
#                 #     request_parameters3 =  request_parameters2.keys() 
#                 # else: 
#                 #     request_parameters3 = request_parameters2

                
#                 # response_parameters = response_info.get('content',{})
#                 # response_parameters1 = response_parameters.get('text',{})

                
                
#                 # if type(response_parameters1)=='dict':
#                 #     response_parameters3 =  response_parameters1.keys() 
#                 # else:
#                 #     response_parameters3 = (response_parameters1)
#                 request_parameters = request_info.get('postData', {}).get('text', {})
#                 response_parameters = response_info.get('content', {}).get('text', {})
                

#                 # try:
#                 #     request_parameters3 = json.loads(request_parameters) if isinstance(request_parameters, str) else request_parameters
#                 #     request_parameters3 = list(request_parameters3.keys()) if isinstance(request_parameters3, dict) else request_parameters3
#                 # except json.JSONDecodeError:
#                 #     request_parameters3 = {}
                

#                 # try:
#                 #     response_parameters3 = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
#                 #     response_parameters3 = list(response_parameters3.keys()) if isinstance(response_parameters3, dict) else response_parameters3
#                 # except json.JSONDecodeError:
#                 #     response_parameters3 = {}
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
                
                
#                 if not isinstance(request_parameters3, list):
#                     request_parameters3 = list(request_parameters3)

                
#                 if query_params:
#                     query_param_keys = [param['name'] for param in query_params]
#                     request_parameters3.extend(query_param_keys)
                
                    

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
#                 dependency_list = {}
#                 dependencies = []
            
#                 # for api, req_params in api_requests.items():
#                 #     
#                 #     for req_url, req_other_params in api_requests.items():
#                 #         if req_url != api and any(param in req_other_params for param in req_params) :
#                 #             dependencies.append(req_url)
#                 #     for res_url, res_params in api_responses.items():
#                 #         if res_params and any(param in res_params for param in req_params):
#                 #             dependencies.append(res_url)
#                 #     if referrer and referrer not in dependencies:
#                 #         dependencies.append(referrer)

#                 #     dependency_list[api] = dependencies

#                 # for apii,res_params in api_responses.items():
#                 #     dependencies1 = []
#                 #     for res_url,res_other_params in api_responses.items():
#                 #         if res_url!=apii and any(param in res_other_params for param in res_params):
#                 #             dependencies1.append(res_url)
#                 #     for req_url,req_params in api_requests.items():
#                 #         if req_params and any(param in req_params for param in res_params):
#                 #             dependencies1.append(req_url)
                    
#                 #     dependency_list[apii] = dependencies1
# ########################################################################################################################
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

#                 path_segments = path.strip('/').split('/')
#                 for other_path in api_requests.keys():
#                     other_segments = other_path.strip('/').split('/')
#                     if any(segment in other_segments for segment in path_segments):
#                         if other_path not in dependencies:
#                             dependencies.append(other_path)

#                 # Ensure the path is a string key
#                 if isinstance(path, str):
#                     dependency_list[path] = dependencies

#                 #todo: - recursively print all the dependencies of the current dependency of a url
#                 #todo: - as looked for the req parameters in req and response parameters of other url
#                 #        also look for the response parameters in other request and response parameters
#                 #todo: - urls that contain query parameters should get the dependencies from the url itself
#                 # GET http://216.48.177.224:4000/ http://216.48.177.224:4000/socket.io/?EIO=3&transport=polling&t=O_ip8b3&sid=iXFOWFt2RrP44ZD2AAAR [{'name': 'EIO', 'value': '3'}, {'name': 'transport', 'value': 'polling'}, {'name': 't', 'value': 'O_ip8b3'}, {'name': 'sid', 'value': 'iXFOWFt2RrP44ZD2AAAR'}]
#                 # dependencies corresponding to this are ['http://216.48.177.224:4000/socket.io/?EIO=3&transport=polling&t=O_imi_P', 'http://216.48.177.224:4000/socket.io/?EIO=3&transport=polling&t=O_imj3k&sid=YGDZq0EIk2T5jTs0AAAQ', 'ws://216.48.177.224:4000/socket.io/?EIO=3&transport=websocket&sid=YGDZq0EIk2T5jTs0AAAQ', 'http://216.48.177.224:4000/socket.io/?EIO=3&transport=polling&t=O_ip8Zr', 'http://216.48.177.224:4000/']
#                 #acceptable dependencies : -'http://216.48.177.224:4000/'


#                 #["UserId", "captchaId", "captcha", "comment", "rating"]
#                 #["status", "id", "UserId", "comment", "rating", "updatedAt", "createdAt"]
#                 # GET http://216.48.177.224:4000/ http://216.48.177.224:4000/rest/user/change-password?current=ha%20b%20sa&new=abcdabcd&repeat=abcdabcd [{'name': 'current', 'value': 'ha%20b%20sa'}, {'name': 'new', 'value': 'abcdabcd'}, {'name': 'repeat', 'value': 'abcdabcd'}]


                
                
                
#                 # print(token_headers)

#                 Endpoints.objects.create(
#                     base_path=base_path,
#                     path=path,
#                     method=method,
#                     query_params=query_params,
#                     requestBody=request_info,
#                     headers=headers,
#                     response_parameters = (response_parameters3),
#                     request_parameters =  (request_parameters3),
#                     responses={'status': response_status},
#                     responsebody = json.loads(response_body),
#                     response_header = response_headers,
#                     authentication=token_headers.get('authorization',{}) ,
#                     referrer = referrer,
#                     dependency_list=dependency_list[path]

                    
#                 )

#             return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)

# #http://216.48.177.224:4000/rest/user/change-password?current=ha%20b%20sa&new=abcdabcd&repeat=abcdabcd:
# #possible dependencies: -base path, http://216.48.177.224:4000/rest,http://216.48.177.224:4000/rest/user,http://216.48.177.224:4000/rest/address, and also the dependencies corresponding to the dependencies of the parent as well




# # updated view for getting the path from the preceeding paths dependency
# # class UploadHarFile(APIView):
# #     queryset = HarFile.objects.all()
# #     serializer_class = FileUploadSerializer
# #     parser_classes = [MultiPartParser, FormParser]

# #     def post(self, request, *args, **kwargs):
# #         file_obj = request.data.get('file_upload')
# #         if not file_obj:
# #             return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

# #         try:
# #             file_name = file_obj.name
# #             if not file_name.endswith('.har'):
# #                 return Response({'error': 'Unsupported file format.'}, status=status.HTTP_400_BAD_REQUEST)

# #             har_content = json.load(file_obj)

# #             if 'log' not in har_content or 'entries' not in har_content['log']:
# #                 return Response({'error': 'Invalid HAR file format.'}, status=status.HTTP_400_BAD_REQUEST)

# #             entries = har_content['log']['entries']
# #             pages = har_content['log']['pages']
# #             for page in pages:
# #                 base_path = page['title']

# #             api_responses = {}
# #             api_requests = {}
# #             dependency_list = {}

# #             for entry in entries:
# #                 request_info = entry['request']
# #                 response_info = entry['response']
# #                 method = request_info['method']

# #                 path = request_info['url']

# #                 query_params = request_info.get('queryString', [])
# #                 response_status = response_info['status']

# #                 headers = request_info.get('headers', [])
# #                 response_headers = response_info.get('headers', [])
# #                 response_body = json.dumps(response_info.get('content', []))

# #                 request_parameters = request_info.get('postData', {}).get('text', {})
# #                 response_parameters = response_info.get('content', {}).get('text', {})

# #                 try:
# #                     request_parameters3 = json.loads(request_parameters) if isinstance(request_parameters, str) else request_parameters
# #                     request_parameters3 = list(request_parameters3.keys()) if isinstance(request_parameters3, dict) else request_parameters3
# #                 except json.JSONDecodeError:
# #                     request_parameters3 = []

# #                 try:
# #                     response_parameters3 = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
# #                     if isinstance(response_parameters3, dict) and 'data' in response_parameters3:
# #                         data_keys = response_parameters3['data'].keys() if isinstance(response_parameters3['data'], dict) else []
# #                         response_parameters3 = list(response_parameters3.keys()) + list(data_keys)
# #                     else:
# #                         response_parameters3 = list(response_parameters3.keys()) if isinstance(response_parameters3, dict) else response_parameters3
# #                 except json.JSONDecodeError:
# #                     response_parameters3 = []

# #                 if not isinstance(request_parameters3, list):
# #                     request_parameters3 = list(request_parameters3)

# #                 if query_params:
# #                     query_param_keys = [param['name'] for param in query_params]
# #                     request_parameters3.extend(query_param_keys)

# #                 token_headers = {}
# #                 non_token_headers = {}

# #                 referrer = ''
# #                 dependency = []
# #                 authentication = []

# #                 for header in headers:
# #                     header_name = header.get('name', '').lower()
# #                     header_value = header.get('value', '')
# #                     if 'token' in header_name or header_name == 'authorization':
# #                         token_headers[header_name] = header_value
# #                         authentication = header_value
# #                     elif header_name == 'referer' or header_name == 'referrer':
# #                         referrer = header_value
# #                     # elif 'token' in header_name or header_name == 'authorization':
# #                     #     dependency.append('/login')
# #                     else:
# #                         non_token_headers[header_name] = header_value

# #                 api_key = f"{method} {path}"
# #                 api_requests[api_key] = request_parameters3
# #                 api_responses[api_key] = response_parameters3

# #             # def add_dependencies(api, dependencies_set):
# #             #     """
# #             #     Recursively add dependencies to the set.
# #             #     """
# #             #     for dep in dependency_list.get(api, []):
# #             #         if dep not in dependencies_set:
# #             #             dependencies_set.add(dep)
# #             #             add_dependencies(dep, dependencies_set)

# #             for api, req_params in api_requests.items():
# #                 dependencies = []
# #                 for req_url, req_other_params in api_requests.items():
# #                     if req_url != api and any(param in req_other_params for param in req_params):
# #                         dependencies.append(req_url)
# #                 for res_url, res_params in api_responses.items():
# #                     if res_params and any(param in res_params for param in req_params):
# #                         dependencies.append(res_url)
# #                 if referrer and referrer not in dependencies:
# #                     dependencies.append(referrer)
# #                 dependency_list[api] = dependencies

            
# #             for api, deps in dependency_list.items():
# #                 full_dependencies = set(deps)
# #                 # for dep in deps:
# #                 #     add_dependencies(dep, full_dependencies)
# #                 dependency_list[api] = list(full_dependencies)

# #             for api_key, request_parameters3 in api_requests.items():
# #                 response_parameters3 = api_responses.get(api_key, [])
# #                 referrer = dependency_list.get(api_key, '')

# #                 method, path = api_key.split(" ", 1)

# #                 Endpoints.objects.create(
# #                     base_path=base_path,
# #                     path=path,
# #                     method=method,
# #                     query_params=query_params,
# #                     requestBody=request_info,
# #                     headers=headers,
# #                     response_parameters=response_parameters3,
# #                     request_parameters=request_parameters3,
# #                     responses={'status': response_status},
# #                     responsebody=json.loads(response_body),
# #                     response_header=response_headers,
# #                     authentication=token_headers.get('authorization', {}),
# #                     referrer=referrer,
# #                     dependency_list=dependency_list[api_key]
# #                 )

# #             def print_dependencies(dependency_list, api, level=0, visited=None):
# #                 if visited is None:
# #                     visited = set()

# #                 if api in visited:
# #                     return
# #                 visited.add(api)

# #                 indent = '  ' * level
# #                 print(f"{indent}{api}")

# #                 for dep in dependency_list.get(api, []):
# #                     print_dependencies(dependency_list, dep, level + 1, visited)

# #             # Example usage with the dependency_list obtained from your code
# #             for api in dependency_list.keys():
# #                 print(f"Dependencies for {api}:")
# #                 print_dependencies(dependency_list, api)
# #                 print()  # For a blank line between different API dependencies

# #             return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

# #         except Exception as e:
# #             return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)


# updated view for getting the path from the preceeding paths dependency
#yaha se start hai main function
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
#                     request_parameters3 = []

#                 try:
#                     response_parameters3 = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
#                     if isinstance(response_parameters3, dict) and 'data' in response_parameters3:
#                         data_keys = response_parameters3['data'].keys() if isinstance(response_parameters3['data'], dict) else []
#                         response_parameters3 = list(response_parameters3.keys()) + list(data_keys)
#                     else:
#                         response_parameters3 = list(response_parameters3.keys()) if isinstance(response_parameters3, dict) else response_parameters3
#                 except json.JSONDecodeError:
#                     response_parameters3 = []

#                 if not isinstance(request_parameters3, list):
#                     request_parameters3 = list(request_parameters3)

#                 if query_params:
#                     query_param_keys = [param['name'] for param in query_params]
#                     request_parameters3.extend(query_param_keys)

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

#                 api_key = f"{method} {path}"
#                 api_requests[api_key] = request_parameters3
#                 api_responses[api_key] = response_parameters3

#             def add_dependencies(api, dependencies_set):
                
#                 for dep in dependency_list.get(api, []):
#                     if dep not in dependencies_set:
#                         dependencies_set.add(dep)
#                         add_dependencies(dep, dependencies_set)

#             for api, req_params in api_requests.items():
#                 dependencies = []
#                 for req_url, req_other_params in api_requests.items():
#                     if req_url != api and any(param in req_other_params for param in req_params):
#                         dependencies.append(req_url)
#                 for res_url, res_params in api_responses.items():
#                     if res_params and any(param in res_params for param in req_params):
#                         dependencies.append(res_url)
#                 if referrer and referrer not in dependencies:
#                     dependencies.append(referrer)
#                 dependency_list[api] = dependencies

            
#             for api, deps in dependency_list.items():
#                 full_dependencies = set(deps)
#                 for dep in deps:
#                     add_dependencies(dep, full_dependencies)
#                 dependency_list[api] = list(full_dependencies)

#             for api_key, request_parameters3 in api_requests.items():
#                 response_parameters3 = api_responses.get(api_key, [])
#                 # referrer = dependency_list.get(api_key, '')

#                 method, path = api_key.split(" ", 1)

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
#                     dependency_list=dependency_list[api_key]
#                 )

#             def print_dependencies(dependency_list, api, level=0, visited=None):
#                 if visited is None:
#                     visited = set()

#                 if api in visited:
#                     return
#                 visited.add(api)

#                 indent = '  ' * level
#                 print(f"{indent}{api}")

#                 for dep in dependency_list.get(api, []):
#                     print_dependencies(dependency_list, dep, level + 1, visited)

#             # Example usage with the dependency_list obtained from your code
#             for api in dependency_list.keys():
#                 print(f"Dependencies for {api}:")
#                 print_dependencies(dependency_list, api)
#                 print()  # For a blank line between different API dependencies

#             return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)


# from urllib.parse import urlparse, parse_qs

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
#                     request_parameters3 = []

#                 try:
#                     response_parameters3 = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
#                     if isinstance(response_parameters3, dict) and 'data' in response_parameters3:
#                         data_keys = response_parameters3['data'].keys() if isinstance(response_parameters3['data'], dict) else []
#                         response_parameters3 = list(response_parameters3.keys()) + list(data_keys)
#                     else:
#                         response_parameters3 = list(response_parameters3.keys()) if isinstance(response_parameters3, dict) else response_parameters3
#                 except json.JSONDecodeError:
#                     response_parameters3 = []

#                 if not isinstance(request_parameters3, list):
#                     request_parameters3 = list(request_parameters3)

#                 if query_params:
#                     query_param_keys = [param['name'] for param in query_params]
#                     request_parameters3.extend(query_param_keys)

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

#             def add_dependencies(api, dependencies_set):
#                 """
#                 Recursively add dependencies to the set.
#                 """
#                 for dep in dependency_list.get(api, []):
#                     if dep not in dependencies_set:
#                         dependencies_set.add(dep)
#                         add_dependencies(dep, dependencies_set)

#             for api, req_params in api_requests.items():
#                 dependencies = []
#                 for req_url, req_other_params in api_requests.items():
#                     if req_url != api and any(param in req_other_params for param in req_params):
#                         dependencies.append(req_url)
#                 for res_url, res_params in api_responses.items():
#                     if res_params and any(param in res_params for param in req_params):
#                         dependencies.append(res_url)
#                 if referrer and referrer not in dependencies:
#                     dependencies.append(referrer)
#                 dependency_list[api] = dependencies

#             # Add indirect dependencies
#             for api, deps in dependency_list.items():
#                 full_dependencies = set(deps)
#                 for dep in deps:
#                     add_dependencies(dep, full_dependencies)
#                 dependency_list[api] = list(full_dependencies)

#             for api_key, request_parameters3 in api_requests.items():
#                 response_parameters3 = api_responses.get(api_key, [])
#                 referrer = dependency_list.get(api_key, '')

#                 Endpoints.objects.create(
#                     base_path=base_path,
#                     path=api_key,
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
#                     dependency_list=dependency_list[api_key]
#                 )

#             def print_dependencies(dependency_list, api, level=0, visited=None):
#                 if visited is None:
#                     visited = set()

#                 if api in visited:
#                     return
#                 visited.add(api)

#                 indent = '  ' * level
#                 print(f"{indent}{api}")

#                 for dep in dependency_list.get(api, []):
#                     print_dependencies(dependency_list, dep, level + 1, visited)

#             # Example usage with the dependency_list obtained from your code
#             for api in dependency_list.keys():
#                 print(f"Dependencies for {api}:")
#                 print_dependencies(dependency_list, api)
#                 print()  # For a blank line between different API dependencies

#             return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)

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
#                     request_parameters3 = []

#                 try:
#                     response_parameters3 = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
#                     if isinstance(response_parameters3, dict) and 'data' in response_parameters3:
#                         data_keys = response_parameters3['data'].keys() if isinstance(response_parameters3['data'], dict) else []
#                         response_parameters3 = list(response_parameters3.keys()) + list(data_keys) #yeh nayi line hai
#                     else:
#                         response_parameters3 = list(response_parameters3.keys()) if isinstance(response_parameters3, dict) else response_parameters3
#                 except json.JSONDecodeError:
#                     response_parameters3 = []

#                 if not isinstance(request_parameters3, list):
#                     request_parameters3 = list(request_parameters3)

#                 if query_params:
#                     query_param_keys = [param['name'] for param in query_params]
#                     request_parameters3.extend(query_param_keys)

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

#                 api_key = f"{method} {path}"
#                 api_requests[api_key] = request_parameters3
#                 api_responses[api_key] = response_parameters3

#             def add_dependencies(api, dependencies_set):
#                 for dep in dependency_list.get(api, []):
#                     if dep not in dependencies_set:
#                         dependencies_set.add(dep)
#                         add_dependencies(dep, dependencies_set)

#             for api, req_params in api_requests.items():
#                 dependencies = set() #yeh nayi line hai
#                 for req_url, req_other_params in api_requests.items():
#                     if req_url != api and any(param in req_other_params for param in req_params):
#                         dependencies.add(req_url) #yeh nayi line hai
#                 for res_url, res_params in api_responses.items():
#                     if res_params and any(param in res_params for param in req_params):
#                         dependencies.add(res_url) #yeh nayi line hai
#                 if referrer:
#                     dependencies.add(referrer) #yeh nayi line hai
#                 dependency_list[api] = list(dependencies) #yeh nayi line hai

#             for api, deps in dependency_list.items():
#                 full_dependencies = set(deps)
#                 for dep in deps:
#                     add_dependencies(dep, full_dependencies)
#                 dependency_list[api] = list(full_dependencies)

#             for api_key, request_parameters3 in api_requests.items():
#                 response_parameters3 = api_responses.get(api_key, [])

#                 method, path = api_key.split(" ", 1)

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
#                     dependency_list=dependency_list[api_key]
#                 )

#             def print_dependencies(dependency_list, api, level=0, visited=None):
#                 if visited is None:
#                     visited = set()

#                 if api in visited:
#                     return
#                 visited.add(api)

#                 indent = '  ' * level
#                 print(f"{indent}{api}")

#                 for dep in dependency_list.get(api, []):
#                     print_dependencies(dependency_list, dep, level + 1, visited)

#             for api in dependency_list.keys():
#                 print(f"Dependencies for {api}:")
#                 print_dependencies(dependency_list, api)
#                 print()

#             return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)

# from django.db.models import Q
# from .models import Endpoint, HarFile
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.response import Response
# from rest_framework import status
# import json

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
#                     request_parameters3 = []

#                 try:
#                     response_parameters3 = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
#                     if isinstance(response_parameters3, dict) and 'data' in response_parameters3:
#                         data_keys = response_parameters3['data'].keys() if isinstance(response_parameters3['data'], dict) else []
#                         response_parameters3 = list(response_parameters3.keys()) + list(data_keys)
#                     else:
#                         response_parameters3 = list(response_parameters3.keys()) if isinstance(response_parameters3, dict) else response_parameters3
#                 except json.JSONDecodeError:
#                     response_parameters3 = []

#                 if not isinstance(request_parameters3, list):
#                     request_parameters3 = list(request_parameters3)

#                 if query_params:
#                     query_param_keys = [param['name'] for param in query_params]
#                     request_parameters3.extend(query_param_keys)

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

#                 # Logic to find dependencies #ye required logic hai
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

#                 if isinstance(path, str):
#                     dependency_list[path] = dependencies
                
                
#                 def find_resembling_paths(base_path):
#                     path_segments = base_path.strip('/').split('/')
#                     queryset = Endpoints.objects.all()
#                     query = Q()
#                     for segment in path_segments:
#                         query |= Q(path__icontains=segment)
#                     resembling_paths = queryset.filter(query)
#                     return resembling_paths

#                 # Example usage of finding resembling paths #ye required logic hai
#                 # base_path = "127.0.0.1/api/rest/user/"
#                 base_path = base_path
#                 resembling_paths = find_resembling_paths(base_path)

#             for endpoint in resembling_paths:
#                 print(endpoint.path)

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

#             # Function to split the path and find resembling paths #ye required logic hai
            

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
#             parameter_to_urls = {}

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

#                 # Create a mapping of parameter keys to URLs
#                 for param in request_parameters3:
#                     if param not in parameter_to_urls:
#                         parameter_to_urls[param] = []
#                     parameter_to_urls[param].append(path)
                
#                 for param in response_parameters3:
#                     if param not in parameter_to_urls:
#                         parameter_to_urls[param] = []
#                     parameter_to_urls[param].append(path)

#             # Generate dependencies based on parameter keys
#             for path, req_params in api_requests.items():
#                 dependencies = set()
#                 for param in req_params:
#                     if param in parameter_to_urls:
#                         dependencies.update(parameter_to_urls[param])
                
#                 dependency_list[path] = list(dependencies)

#             for path, res_params in api_responses.items():
#                 dependencies = set()
#                 for param in res_params:
#                     if param in parameter_to_urls:
#                         dependencies.update(parameter_to_urls[param])
                
#                 if path in dependency_list:
#                     dependency_list[path].extend(list(dependencies))
#                 else:
#                     dependency_list[path] = list(dependencies)

#             # Store the endpoints and dependencies in the database
#             for path in api_requests:
#                 Endpoints.objects.create(
#                     base_path=base_path,
#                     path=path,
#                     method=api_requests[path].get('method', ''),
#                     query_params=api_requests[path].get('query_params', []),
#                     requestBody=api_requests[path].get('requestBody', {}),
#                     headers=api_requests[path].get('headers', []),
#                     response_parameters=api_responses.get(path, []),
#                     request_parameters=api_requests[path].get('request_parameters', []),
#                     responses={'status': api_responses[path].get('status', '')},
#                     responsebody=api_responses[path].get('responsebody', {}),
#                     response_header=api_responses[path].get('response_header', []),
#                     authentication=api_requests[path].get('authentication', {}),
#                     referrer=api_requests[path].get('referrer', ''),
#                     dependency_list=dependency_list.get(path, [])
#                 )

#             return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)


#31-07-24
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_param = False
#         self.urls = []

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, param, url):
#         node = self.root
#         for char in param:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end_of_param = True
#         if url not in node.urls:
#             node.urls.append(url)

#     def search_similar_params(self, param):
#         node = self.root
#         similar_urls = set()

#         def dfs(current_node, current_char_idx):
#             if current_node.is_end_of_param:
#                 similar_urls.update(current_node.urls)
#             for char, child_node in current_node.children.items():
#                 if current_char_idx < len(param) and char == param[current_char_idx]:
#                     dfs(child_node, current_char_idx + 1)
#                 else:
#                     dfs(child_node, current_char_idx)
        
#         dfs(node, 0)
#         return list(similar_urls)




# import json
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import *
# from .models import *
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
# from collections import defaultdict
# import pytrie
# from urllib.parse import urlparse
# from collections import defaultdict

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
#             dependency_list = defaultdict(set)
#             trie = pytrie.StringTrie()

#             for entry in entries:
#                 request_info = entry['request']
#                 response_info = entry['response']
#                 method = request_info['method']

#                 cookies = request_info['cookies']
#                 path = request_info['url']
#                 # parsed_url = urlparse(full_url)
#                 # base_path = f"{parsed_url.scheme}://{parsed_url.netloc}"
#                 # path = parsed_url.path

#                 # path_trie.insert(path)


#                 query_params = request_info.get('queryString', [])
#                 response_status = response_info['status']

#                 headers = request_info.get('headers', [])
#                 response_headers = response_info.get('headers', [])
#                 response_body = json.dumps(response_info.get('content', []))

#                 request_parameters = request_info.get('postData', {}).get('text', {})
#                 response_parameters = response_info.get('content', {}).get('text', {})

#                 # try:
#                 #     request_parameters3 = json.loads(request_parameters) if isinstance(request_parameters, str) else request_parameters
#                 #     request_parameters3 = list(request_parameters3.keys()) if isinstance(request_parameters3, dict) else request_parameters3
#                 # except json.JSONDecodeError:
#                 #     request_parameters3 = {}

#                 # try:
#                 #     response_parameters3 = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
#                 #     if isinstance(response_parameters3, dict) and 'data' in response_parameters3:
#                 #         data_keys = response_parameters3['data'].keys() if isinstance(response_parameters3['data'], dict) else []
#                 #         response_parameters3 = list(response_parameters3.keys()) + list(data_keys)
#                 #     else:
#                 #         response_parameters3 = list(response_parameters3.keys()) if isinstance(response_parameters3, dict) else response_parameters3
#                 # except json.JSONDecodeError:
#                 #     response_parameters3 = {}
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

#                 if not isinstance(request_parameters3, list):
#                     request_parameters3 = list(request_parameters3)

#                 if query_params:
#                     query_param_keys = [param['name'] for param in query_params]
#                     request_parameters3.extend(query_param_keys)


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

#                 # Insert request and response parameters into the trie
#                 for param in request_parameters3:
#                     if isinstance(param, dict):
#                         param = json.dumps(param)  # Convert dict to string
#                     trie[param] = trie.get(param, set())
#                     trie[param].add(path)

#                 for param in response_parameters3:
#                     if isinstance(param, dict):
#                         param = json.dumps(param)  # Convert dict to string
#                     trie[param] = trie.get(param, set())
#                     trie[param].add(path)

#             # Generate dependencies based on parameter keys
#             for path, req_params in api_requests.items():
#                 dependencies = set()
#                 for param in req_params:
#                     if isinstance(param, dict):
#                         param = json.dumps(param)  # Convert dict to string
#                     dependencies.update(trie.get(param, set()))

#                 dependency_list[path].update(dependencies)

#             for path, res_params in api_responses.items():
#                 dependencies = set()
#                 for param in res_params:
#                     if isinstance(param, dict):
#                         param = json.dumps(param)  # Convert dict to string
#                     dependencies.update(trie.get(param, set()))

#                 dependency_list[path].update(dependencies)

#             # Store the endpoints and dependencies in the database
#             for path in api_requests:
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
#                     authentication=token_headers.get('authorization', ''),
#                     referrer=referrer,
#                     dependency_list=list(dependency_list.get(path, []))  # Convert set to list
#                 )

#             return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             print(f"Error: {e}")  # Print the error message
#             return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)






# import json
# import rest_framework
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import *
# from .models import *
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
# from urllib.parse import urlparse

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_path = False
#         self.paths = []
#         self.parameters = set()

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, path, parameters):
#         node = self.root
#         segments = path.strip('/').split('/')
#         for segment in segments:
#             if segment not in node.children:
#                 node.children[segment] = TrieNode()
#             node = node.children[segment]
#         node.is_end_of_path = True
#         node.paths.append(path)
#         node.parameters.update(parameters)

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

#     def search_similar_parameters(self, parameters):
#         node = self.root
#         similar_parameters = set()

#         def dfs(current_node, current_parameters):
#             similar_parameters.update(current_node.parameters)
#             for segment, child_node in current_node.children.items():
#                 if segment in current_parameters:
#                     dfs(child_node, current_parameters)

#         dfs(node, parameters)
#         return list(similar_parameters)

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
#             api_responses = {}
#             api_requests = {}
#             path_trie = Trie()
#             dependency_list = {}
#             pages = har_content['log']['pages']
#             for page in pages:
#                 base_path = page['title']

#             for entry in entries:
#                 request_info = entry['request']
#                 response_info = entry['response']
#                 method = request_info['method']
#                 full_url = request_info['url']

#                 parsed_url = urlparse(full_url)
#                 path = parsed_url.path

#                 request_parameters = request_info.get('postData', {}).get('text', {})
#                 response_parameters = response_info.get('content', {}).get('text', {})

#                 try:
#                     request_parameters = json.loads(request_parameters) if isinstance(request_parameters, str) else request_parameters
#                     request_parameters = list(request_parameters.keys()) if isinstance(request_parameters, dict) else request_parameters
#                 except json.JSONDecodeError:
#                     request_parameters = []

#                 try:
#                     response_parameters = json.loads(response_parameters) if isinstance(response_parameters, str) else response_parameters
#                     response_parameters = list(response_parameters.keys()) if isinstance(response_parameters, dict) else response_parameters
#                 except json.JSONDecodeError:
#                     response_parameters = []

#                 if not isinstance(request_parameters, list):
#                     request_parameters = list(request_parameters)

#                 # Insert path and parameters into Trie
#                 path_trie.insert(path, request_parameters + response_parameters)

#                 # Store requests and responses for dependency finding
#                 api_requests[path] = request_parameters
#                 api_responses[path] = response_parameters

#                 # Dependencies based on similar parameters
#                 dependencies = []
#                 for req_url, req_params in api_requests.items():
#                     if req_url != path and any(param in req_params for param in request_parameters):
#                         dependencies.append(req_url)
#                 for res_url, res_params in api_responses.items():
#                     if res_params and any(param in res_params for param in request_parameters):
#                         if res_url not in dependencies:
#                             dependencies.append(res_url)
                
#                 # Dependencies based on similar response parameters
#                 for req_url, req_params in api_requests.items():
#                     if req_url != path and any(param in req_params for param in response_parameters):
#                         dependencies.append(req_url)
#                 for res_url, res_params in api_responses.items():
#                     if res_params and any(param in res_params for param in response_parameters):
#                         if res_url not in dependencies:
#                             dependencies.append(res_url)
                            

#                 # Add dependencies based on similar paths
#                 similar_paths = path_trie.search_similar_paths(path)
#                 for similar_path in similar_paths:
#                     if similar_path != path and similar_path not in dependencies:
#                         dependencies.append(similar_path)

#                 # Find similar parameters across all endpoints
#                 similar_parameters = path_trie.search_similar_parameters(request_parameters + response_parameters)
#                 for param in similar_parameters:
#                     for req_url, req_params in api_requests.items():
#                         if param in req_params and req_url not in dependencies:
#                             dependencies.append(req_url)
#                     for res_url, res_params in api_responses.items():
#                         if param in res_params and res_url not in dependencies:
#                             dependencies.append(res_url)

#                 if isinstance(path, str):
#                     dependency_list[path] = dependencies

#                 Endpoints.objects.create(
#                     base_path=base_path,
#                     path=path,
#                     method=method,
#                     query_params=request_info.get('queryString', []),
#                     requestBody=request_info,
#                     headers=request_info.get('headers', []),
#                     response_parameters=response_parameters,
#                     request_parameters=request_parameters,
#                     responses={'status': response_info['status']},
#                     responsebody=json.loads(response_info.get('content', {}).get('text', '{}')),
#                     response_header=response_info.get('headers', []),
#                     authentication={},
#                     referrer='',
#                     dependency_list=dependency_list[path]
#                 )

#             return Response({'message': 'success!!'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': f'Error processing file: {e}'}, status=status.HTTP_400_BAD_REQUEST)


# 31/07/24
# import json
# import rest_framework
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import *
# from .models import *
# import haralyzer
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
# from urllib.parse import urlparse

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_path = False
#         self.paths = []
#         # self.parameters = set()

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
#         # node.parameters.update(parameters)

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

#     def search_similar_parameters(self, parameters):
#         node = self.root
#         similar_parameters = set()

#         def dfs(current_node, current_parameters):
#             similar_parameters.update(current_node.parameters)
#             for segment, child_node in current_node.children.items():
#                 if segment in current_parameters:
#                     dfs(child_node, current_parameters)

#         dfs(node, parameters)
#         return list(similar_parameters)

    

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
#                     if isinstance(response_parameters3, dict) and 'data' in response_parameters3:
#                         data_keys = response_parameters3['data'].keys() if isinstance(response_parameters3['data'], dict) else []
#                         response_parameters3 = list(response_parameters3.keys()) + list(data_keys)
#                     else:
#                         response_parameters3 = list(response_parameters3.keys()) if isinstance(response_parameters3, dict) else response_parameters3
#                 except json.JSONDecodeError:
#                     response_parameters3 = {}

#                 if not isinstance(request_parameters3, list):
#                     request_parameters3 = list(request_parameters3)

#                 if query_params:
#                     query_param_keys = [param['name'] for param in query_params]
#                     request_parameters3.extend(query_param_keys)

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
#                     # elif 'token' in header_name or header_name == 'authorization':
#                     #     dependency.append('/login')
#                     else:
#                         non_token_headers[header_name] = header_value

#                 api_requests[path] = request_parameters3
#                 api_responses[path] = response_parameters3

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
#                 #add trie data structure to filter out the dependencies from request and response parameters

#                 # Adding pattern matching dependencies using Trie
#                 similar_paths = path_trie.search_similar_paths(path)
#                 for similar_path in similar_paths:
#                     if similar_path != path and similar_path not in dependencies:
#                         dependencies.append(similar_path)

#                 if isinstance(path, str):
#                     dependency_list[path] = dependencies

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