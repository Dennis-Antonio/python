
class Empregado:
    def __init__(self, nome,salario_base):
        self.nome = nome
        self.salario_base = salario_base
    
    def calculara_salario(self):
        return self.salario_base

class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus_fixo):
        super().__init__(nome, salario_base)
        self.bonus_fixo = bonus_fixo

    def calcular_salario(self):
        return self.salario_base + self.bonus_fixo

class Vendedo(Empregado):
   def __init__(self, nome, salario_base, vendas, comissao):
        super().__init__(nome, salario_base)
        self.vendas = vendas
        self.comissao = comissao
    
   def calcular_salario(self):
        return self.salario_base + (self.vendas * self.comissao)
   
gerente = Gerente("Dennis", 5000, 1000)
print(f"Salário total do gerente {gerente.nome}: R$ {gerente.calcular_salario():.2f}")

vendedor = Vendedo("Ana", 2000, 50000, 0.05)
print(f"Salário total do vendedor {vendedor.nome}: R$ {vendedor.calcular_salario():.2f}")