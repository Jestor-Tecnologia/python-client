
class Filter:
    def __init__(self, field: str, value: str, operator: str, type: str = 'string'):
        self.field = field
        self.type = type
        self.value = value
        self.operator = operator
    
    def serialize(self):
        return self.__dict__