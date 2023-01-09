from typing import List
from jestor.Client import Client
from jestor.filter.Filter import Filter

class Table:
    def __init__(self, token, org, table_name, depth = None):
        self.client = Client(token, org, depth)
        self.table_name = table_name
        
    def __getattr__(self, name, arguments: list = None):
        def function(arguments: list = None):
            data = {'arguments': [self.table_name]}
            
            if (arguments != None):
                data = self.appendArgs(arguments, data)
                    
            return self.client.jestorCallFunctions(name, data)
        return function
        
        
    def get(self, filters: List[Filter] = None, limit: int = 100, page: int = 1, sort: str = None, fields_to_select = None, fetch_type = 'single'): 
        if (filters != None):
            filters = self.serializeFilters(filters)
        
        arguments = {'arguments': [
                self.table_name,
                filters,
                limit,
                page,
                sort,
                fields_to_select,
                fetch_type
            ]
        }
        
        return self.client.jestorCallFunctions('fetch', arguments)
    
    def insert(self, data):
        arguments = {'arguments': [self.table_name, data]}
        return self.client.jestorCallFunctions('createObject', arguments)
    
    def update(self, recordId: int, data: dict, additional_action_data: list = []):
        data.update({'id_'+self.table_name: recordId})
        arguments = {'arguments': [self.table_name, data, additional_action_data]}
        print(data)
        return self.client.jestorCallFunctions('updateObject', arguments)
    
    def delete(self, recordId: int):
        arguments = {'arguments': [self.table_name, recordId]}
        return self.client.jestorCallFunctions('removeObject', arguments)
    
    def serializeFilters(self, filters: List[Filter]):
        serializedFilters = []
        
        for filter in filters:
            serializedFilters.append(filter.serialize())
            
        return serializedFilters
    
    def appendArgs(self, args, data):
        for argument in args:
            if isinstance(argument, Filter):
                argument = self.serializeFilters(argument)
                
            data['arguments'].append(argument)
                
        return data
    
    