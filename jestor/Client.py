import requests
import json

from jestor.exception.JestorApiException import JestorApiException

class Client:
    def __init__(self, token, org):
        self.token = token 
        self.org = org
        
    def jestorCallFunctions(self, path, arguments = {}, files = None):
        try:
            headers = {}
            headers["Accept"] = "application/json"
            headers["Authorization"] = f'Bearer {self.token}'
            headers["User-Agent"] = 'Jestor Python Client'
            
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