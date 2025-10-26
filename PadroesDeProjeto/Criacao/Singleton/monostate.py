class Monostate:
    __estado = {}
    
    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__estado
        return obj
    
    
m1 = Monostate()
print(f"Instância 1: {id(m1)}")
print(m1.__dict__)

m2 = Monostate()
print(f"Instância 2: {id(m2)}")
print(m2.__dict__)

m1.nome = "Felicity"
print(m1.__dict__)
print(m2.__dict__)