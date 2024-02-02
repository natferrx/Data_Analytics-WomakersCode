# PRÁTICA 5 - Exercícios Classes e Objetos

'''
1. Crie uma classe que modele o objeto "carro".
2. Um carro tem os seguintes atributos: ligado, cor, modelo,
velocidade.
3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,
desacelera.
4. Crie uma instância da classe carro.
5. Faça o carro "andar" utilizando os métodos da sua classe.
6. Faça o carro "parar" utilizando os métodos da sua classe.
'''

# Criando uma classe que modele o objeto "carro", com os seguintes atributos: ligado, cor, modelo, velocidade.

class Carro: 
    def __init__(self):
        self.ligado = False
        self.velocidade = 0
        self.velocidade_max = 200
        self.velocidade_min = 0
        self.cor = "Branco"
        self.modelo = "SUV"

# 3. Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera. 
        
    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
    
    def aumentar_velocidade(self):
        if not self.ligado:
            return
        
        if self.velocidade < self.velocidade_max:
            self.velocidade += 1
        
    def diminuir_velocidade(self):
        if not self.ligado:
            return
        
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 1

# 4. Crie uma instância da classe carro.

carro_maria = Carro()
carro_joao = Carro()

# 5. Faça o carro "andar" utilizando os métodos da sua classe.

carro_maria.ligar()

for _ in range(10):
    carro_maria.aumentar_velocidade()

# 6. Faça o carro "parar" utilizando os métodos da sua classe.
    
for _ in range(10):
    carro_maria.diminuir_velocidade()

carro_maria.desligar()

print('carro_maria está ligado? {}'.format(carro_maria.ligado))
print('carro_maria está com qual velocidade? {}'.format(carro_maria.velocidade))

