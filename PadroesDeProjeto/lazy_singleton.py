class LazySingleton():
    
    __instance = None
    
    def __init__(self):
        if not LazySingleton.__instance:
            print("P método __init__ foi chamado...")
        else:
            print(f"Instância já criada: {self.get_instance()}")
            
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance
    
ls1 = LazySingleton().get_instance()
print(f"Instância 1: {id(ls1)}")

ls2 = LazySingleton().get_instance()
print(f"Instância 2: {id(ls2)}")