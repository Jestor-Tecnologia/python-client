import requests
import json
import os

from jestor.exception.JestorApiException import JestorApiException

class Client:
    def __init__(self, token, org, depth = None):
        self.token = token 
        self.org = org
        self.depth = depth

    def jestorCallFunctions(self, path, arguments = {}, files = None):
        try:
            headers = {}
            headers["Accept"] = "application/json"
            headers["Authorization"] = f'Bearer {self.token}'
            headers['x-low-code-trigger-depth'] = self.depth

            jestor_user_agent = os.getenv('jestor_user_agent')
            if jestor_user_agent is not None:
                headers["User-Agent"] = f'jestor-python-sdk/{jestor_user_agent}'
            else:
                headers["User-Agent"] = 'jestor-python-sdk'

            jestor_local = os.getenv('jestor_host_local')
            if jestor_local is not None:
                url = f'http://{jestor_local}/v3/low-code-execution/{path}'
                headers["Host"] = f'{self.org}.api.local.jestor.com'
            else:
                url = f'https://{self.org}.api.jestor.com/v3/low-code-execution/{path}'
            
            response = requests.post(
                url,
                data = json.dumps(arguments), 
                files = files,
                headers = headers
            )
            
            if response.status_code > 299:
                raise JestorApiException(response)
            
            response_json = response.json()

            return response_json['data']
        except requests.exceptions.RequestException as e:
            raise e
        except JestorApiException as e:
            raise e