from typing import List
from sdk.Client import Client
from sdk.Filter.Filter import Filter
from sdk.Table import Table
from sdk.User import User
from sdk.File import File

class Jestor:
    def __init__(self, token, org):
        self.token = token
        self.org = org
    
    def client(self)-> Client:
        return Client(self.token, self.org)
    
    def table(self, table_name) -> Table:
        return Table(self.token, self.org, table_name)
    
    def user(self) -> User:
        return User(self.token, self.org)
    
    def file(self, table: str, id: int = None, field: str = None) -> File:
        return File(self.token, self.org, table, id, field)
    
    def __getattr__(self, name, arguments = None):
        def function(arguments = None):
            data = {'arguments': []}
            
            if arguments != None:
                data = self.appendArgs(arguments, data)
            
            return self.client().jestor_call_functions(name, data)
        return function
    
    def appendArgs(self, arguments, data):
        for argument in arguments:
            if isinstance(argument, list) and isinstance(argument[0], Filter):
                argument = self.serializeFilters(argument)
                
            data['arguments'].append(argument)
                
        return data
    
    def serializeFilters(self, filters: List[Filter]):
        serializedFilters = []
        
        for filter in filters:
            serializedFilters.append(filter.serialize())
            
        return serializedFilters
    
        