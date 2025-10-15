
class Curso:
    def __init__(self, nome: str = 'Curso Padrão', carga_horaria: int = 45) -> None:
        self.nome = nome
        self.carga_horaria = carga_horaria

curso1 = Curso()
curso2 = Curso(nome="Padrões de Projetos em Python")
curso3 = Curso(nome="Orquestração de Containers com Kubernetes", carga_horaria=23)

print(curso1.__dict__)
print(curso2.__dict__)
print(curso3.__dict__) 