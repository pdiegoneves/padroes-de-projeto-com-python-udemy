class SanidadeCheck:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(SanidadeCheck, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
    
    
    def __init__(self):
        self.__servidores = []
        
    def checar_servidor(self, srv):
        print(f"Checando o servidor {self.__servidores[srv]}")
        
    def add_servidores(self):
        self.__servidores.append("Servidor 1")
        self.__servidores.append("Servidor 2")
        self.__servidores.append("Servidor 3")
        self.__servidores.append("Servidor 4")
        
    def mudar_servidor(self):
        self.__servidores.pop()
        self.__servidores.append("Servidor 5")
        
    def get_servidores(self):
        return self.__servidores
        
sc1 = SanidadeCheck()
sc2 = SanidadeCheck()

sc1.add_servidores()
print("Cronograma de checagem de sanidades dos servidores A...")
for i, _ in enumerate(sc1.get_servidores()):
    sc1.checar_servidor(i)
    
sc1.mudar_servidor()

print("Cronograma de checagem de sanidades dos servidores B...")
for i, _ in enumerate(sc2.get_servidores()):
    sc2.checar_servidor(i)