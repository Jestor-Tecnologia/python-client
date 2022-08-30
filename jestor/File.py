import json
from jestor.Client import Client

class File:
    files = []
    def __init__(self, token: str, org: str, table: str, id: int = None, field: str = None):
        self.client = Client(token, org)
        self.table = table
        self.id = id
        self.field = field
        
        if id != None and field != None:
            self.files = self.get()
        
    def get(self):
        arguments = {'arguments': [
                self.table,
                self.id,
                self.field
            ]
        }
        
        response = self.client.jestorCallFunctions('getFiles', arguments)
        return response['data']
        
    def add(self, configFile: dict):
        arguments = {'arguments': [
                self.table,
                configFile,
                self.id,
                self.field
            ]
        }
        
        response = self.client.jestorCallFunctions('addFile', arguments)
        
        self.appendFiles(response['data'])
        
        return self.files
    
    def update(self, fileId: str, configFile: dict):       
        arguments = {'arguments': [
                self.table,
                configFile,
                fileId,
                self.id,
                self.field
            ]
        }
        
        response = self.client.jestorCallFunctions('updateFile', arguments)
        
        self.removeFiles(fileId)
        self.appendFiles(response['data'])
        
        return self.files
    
    def delete(self, fileId: str):       
        arguments = {'arguments': [
                self.table,
                fileId,
                self.id,
                self.field,
            ]
        }
        
        self.client.jestorCallFunctions('deleteFile', arguments)
        self.removeFiles(fileId)
        
        return self.files
    
    def appendFiles(self, files):
        for file in files:
            if file not in self.files:
                self.files.append(file)
                
    def removeFiles(self, fileId: str): 
        for file in self.files:
            if file['id'] == fileId:
                self.files.remove(file)
    
    def toJson(self):
        return json.dumps(self.files)
        
            
    