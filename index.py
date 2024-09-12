class Aluno:
    def __init__(self, nome, nota1=0.0, nota2=0.0):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    # Métodos para acessar e definir o nome
    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    # Métodos para acessar e definir as notas
    def set_nota1(self, nota1):
        self.__nota1 = nota1

    def get_nota1(self):
        return self.__nota1

    def set_nota2(self, nota2):
        self.__nota2 = nota2

    def get_nota2(self):
        return self.__nota2

    # Método para calcular a média das notas
    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2

    # Método para exibir o nome e a média
    def exibir_nome_e_media(self):
        media = self.calcular_media()
        print(f"Nome: {self.__nome}, Média: {media:.2f}")

aluno = Aluno("Dennis", 6.5, 9)
aluno.exibir_nome_e_media() 
