from typing import List
from jestor.Client import Client
from jestor.filter.Filter import Filter
from jestor.Table import Table
from jestor.User import User
from jestor.File import File

class Jestor:
    def __init__(self, token, org, depth = None):
        self.token = token
        self.org = org
        self.depth = depth
    
    def client(self)-> Client:
        return Client(self.token, self.org, self.depth)
    
    def table(self, table_name) -> Table:
        return Table(self.token, self.org, table_name, self.depth)
    
    def user(self) -> User:
        return User(self.token, self.org)
    
    def file(self, table: str, id: int = None, field: str = None) -> File:
        return File(self.token, self.org, table, id, field)
    
    def __getattr__(self, name, arguments = None):
        def function(arguments = None):
            data = {'arguments': []}
            
            if arguments != None:
                data = self.appendArgs(arguments, data)
            
            return self.client().jestorCallFunctions(name, data)
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
    
        