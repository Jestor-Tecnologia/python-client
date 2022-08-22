from typing import List
from sdk.Client import Client
from sdk.Filter.Filter import Filter

class Table:
    def __init__(self, token, org, table_name):
        self.client = Client(token, org)
        self.table_name = table_name
        
    def __getattr__(self, name, arguments):
        def function(arguments):
            arguments = {'arguments': [
                    self.table_name,
                    arguments
                ]
            }
            
            return self.client.jestor_call_functions(name, arguments)
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
        
        response = self.client.jestor_call_functions('fetch', arguments)
        
        return response['data']
    
    def insert(self, data):
        arguments = {'arguments': [self.table_name, data]}
        return self.client.jestor_call_functions('createObject', arguments)
    
    def update(self, data: object, additional_action_data):
        arguments = {'arguments': [self.table_name, data, additional_action_data]}
        return self.client.jestor_call_functions('updateObject', arguments)
    
    def delete(self, record_id):
        arguments = {'arguments': [self.table_name, record_id]}
        return self.client.jestor_call_functions('removeObject', arguments)
    
    def serializeFilters(self, filters: List[Filter]):
        serializedFilters = []
        
        for filter in filters:
            serializedFilters.append(filter.serialize())
            
        return serializedFilters
    
    