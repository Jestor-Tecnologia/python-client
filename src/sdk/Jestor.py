from sdk.Client import Client
from sdk.Table import Table
from sdk.User import User

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
    
    def __getattr__(self, name, arguments = None):
        def function(arguments):
            arguments = {'arguments': arguments}
            
            return self.client().jestor_call_functions(name, arguments)
        return function
    
    
        