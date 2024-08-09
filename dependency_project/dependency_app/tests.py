import json
from haralyzer import HarParser
har_parser = []

def parse_har_file(har_file_path):
    with open(har_file_path, 'r', encoding='utf-8') as f:
        har_parser = HarParser(json.loads(f.read()))
    return har_parser['log']['entries']


def extract_params_from_response(response):
    try:
        response_content = json.loads(response['content']['text'])
        if response_content['data']:
            return response_content['data'].keys() 
    
    except:
        return []

def extract_params_from_request(request):
    try:
        request_content = json.loads(request['postData']['text'])
        return request_content.keys()
    except:
        return []
    
#new method to find dependencies

    
def dependencies(har_entries):
    api_responses = {}
    api_requests = {}


    for entry in har_entries:
        request = entry['request']
        response = entry['response']

        url = request['url']
        

        request_params = extract_params_from_request(request)
        print(url)
        print('-'*80)
        print(request_params)
        print('-'*80)
        response_params = extract_params_from_response(response)
        print(url)
        print('-'*80)
        print(response_params)
        
        print('-'*80)
        
        api_responses[url] = response_params
        api_requests[url] = request_params
        
    
    dependency_list = {}
    for api, req_params in api_requests.items():
        dependencies = []
        for res_params in api_responses.items():
            if any(param in res_params for param in req_params):
                dependencies.append(api)
        dependency_list[url] = dependencies

    return dependency_list
    

har_file_path = 'Juiceshop1.har'
with open(har_file_path, 'r', encoding='utf-8') as f:
        har_parser = HarParser(json.loads(f.read()))

har_entries = har_parser.har_data["entries"]


# dependencies_list = dependencies(har_entries)
# new way to find dependency list

print('-'*80)

