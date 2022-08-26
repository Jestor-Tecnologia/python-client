from typing import List
from sdk.Client import Client
from sdk.Filter.Filter import Filter

class User:
    def __init__(self, token, org):
        self.client = Client(token, org)
        
    def get(self, filters: List[Filter] = None, limit: int = 100, page: int = 1, sort: str = None):
        if (filters != None):
            filters = self.serializeFilters(filters)
            
        arguments = {'arguments': [
                filters,
                limit,
                page,
                sort
            ]
        }
        
        return self.client.jestor_call_functions('fetchUsers', arguments)
    
    def __getattr__(self, name, arguments = None):
        def function(arguments):
            arguments = {'arguments': arguments}
            
            return self.client.jestor_call_functions(name, arguments)
        return function
    
    def serializeFilters(self, filters: List[Filter]):
        serializedFilters = []
        
        for filter in filters:
            serializedFilters.append(filter.serialize())
            
        return serializedFilters