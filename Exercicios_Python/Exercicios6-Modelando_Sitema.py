# PRÁTICA 6 - Exercícios - Modelando um Sistema

'''
1. O banco Banco Delas é um banco moderno e eficiente, com
vantagens exclusivas para clientes mulheres.
Modele um sistema orientado a objetos para representar contas
correntes do Banco Delas seguindo os requisitos abaixo.
● Cada conta corrente pode ter um ou mais clientes como
titular.
● O banco controla apenas o nome, o telefone e a renda
mensal de cada cliente.
● A conta corrente apresenta um saldo e uma lista de
operações de saques e depósitos.
● Quando a cliente fizer um saque, diminuiremos o saldo da
conta corrente. Quando ela fizer um depósito,
aumentaremos o saldo.
● Clientes mulheres possuem em suas contas um cheque
especial de valor igual à sua renda mensal, ou seja, elas
podem sacar valores que deixam a sua conta com valor
negativo até renda_mensal.
● Clientes homens por enquanto não têm direito a cheque
especial.
Para modelar seu sistema, utilize obrigatoriamente os conceitos
"classe", "herança", "propriedades", "encapsulamento" e "classe
abstrata".
'''

from abc import ABC, abstractmethod

# Classe abstrata Cliente que define a estrutura básica do cliente
class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal

    @abstractmethod
    def tem_cheque_especial(self):
        pass

# ClienteMulher herda de Cliente e implementa o método abstrato tem_cheque_especial
class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
        self.cheque_especial = renda_mensal

    def tem_cheque_especial(self):
        return True

# ClienteHomem herda de Cliente e implementa o método abstrato tem_cheque_especial
class ClienteHomem(Cliente):
    def tem_cheque_especial(self):
        return False

# Classe ContaCorrente representa a conta corrente
class ContaCorrente:
    def __init__(self):
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f'Depósito: +{valor}')

    def sacar(self, valor, cliente):
        if cliente.tem_cheque_especial() or self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(f'Saque: -{valor}')
        else:
            print('Saldo insuficiente!')

# Exemplo de uso do sistema
cliente_mulher = ClienteMulher("Maria", "123456789", 5000)
cliente_homem = ClienteHomem("João", "987654321", 4000)

conta_maria = ContaCorrente()
conta_joao = ContaCorrente()

# Simulando uma mulher que tem cheque especial
'''
conta_maria.depositar(2000)
conta_maria.sacar(3000, cliente_mulher)

print(f"Saldo conta Maria: {conta_maria.saldo}")
print(f"Operações conta Maria: {conta_maria.operacoes}")
'''

# Simulando um homem que não tem cheque especial
conta_joao.depositar(1500)
conta_joao.sacar(2000, cliente_homem)

print(f"Saldo conta João: {conta_joao.saldo}")
print(f"Operações conta João: {conta_joao.operacoes}")
