import requests
import json

from sdk.Exception.ErrorApi import ErrorApi

class Client:
    def __init__(self, token, org):
        self.token = token 
        self.org = org
        
    def jestorCallFunctions(self, path, arguments = {}, files = None):
        try:
            headers = {}
            headers["Accept"] = "application/json"
            headers["Authorization"] = f'Bearer {self.token}'
            headers["Host"] = f'https://{self.org}.jestor.com'
            
            url = f'https://{self.org}.jestor.com/v3/low-code-execution/{path}'
            
            response = requests.post(
                url,
                data = json.dumps(arguments), 
                files = files,
                headers = headers
            )
            
            response_json = response.json()
            
            if response.status_code > 299:
                return self.errorApi(response.status_code, response_json['data']['message'])
            
            return response_json
        except requests.exceptions.RequestException as e: 
            raise e
        except ErrorApi as e: 
            raise e
        
    def errorApi(self, status_code, message):
        raise ErrorApi(status_code, message)