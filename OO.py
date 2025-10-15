from datetime import datetime

class Pessoa:
    def __init__(self: object, nome: str) -> None:
        self.__nome = nome
        self.__nascimento = datetime.now()


    def __str__(self) -> str:
        return self.__nome
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} <{id(self)}>: {self.__nome}"
    
class Carro:
    def __init__(self: object, is_sedan: bool = False) -> None:
        self.__is_sedan = is_sedan
        self.__velocidade = 0
        self.__motorista = None

    def __str__(self) -> str:
        if self.__motorista:
            return f"Carro do(a) {self.__motorista}"
        return "Carro sem motorista"
        
    def digitir(self: object, motorista: Pessoa, velocidade: int) -> None:
        self.__motorista = motorista
        self.acelerar(velocidade)

    def acelerar(self: object, velocidade: int) -> None:
        self.__velocidade += velocidade

    def parar(self: object) -> None:
        self.__velocidade = 0

    
if __name__ == "__main__":
    angelina = Pessoa("Angelina")
    fusca = Carro()
    print(angelina)
    print(fusca)
    fusca.digitir(angelina, 100)
    print(fusca.__dict__)