class University(type):
    
    def __call__(self, *args, **kwds):
        print(f"==== Estes são os argumentos {args}")
        return super().__call__(*args, **kwds)
    
    
class Geek(metaclass=University):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        

geek = Geek(1, 2)
print(geek)