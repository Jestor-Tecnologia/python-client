from typing import List
from jestor.Client import Client
from jestor.filter.Filter import Filter

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
        
        return self.client.jestorCallFunctions('fetchUsers', arguments)
    
    def __getattr__(self, name, arguments = None):
        def function(arguments = None):
            data = {'arguments': []}
            
            if arguments != None:
                data = self.appendArgs(arguments, data)
            
            return self.client().jestorCallFunctions(name, data)
        return function
    
    def serializeFilters(self, filters: List[Filter]):
        serializedFilters = []
        
        for filter in filters:
            serializedFilters.append(filter.serialize())
            
        return serializedFilters