#PRÁTICA 1 - Aplicação conceitos iniciais Python

'''
1. Faça um Programa que peça dois números e realize as principais operações: 
soma, subtração, multiplicação, divisão
'''
'''
Numero1 = int(input("Entre com o primeiro número inteiro: "))
Numero2 = int(input("Entre com o segundo número inteiro: "))
soma = Numero1 + Numero2
subtracao = Numero1 - Numero2
multiplicacao = Numero1 * Numero2
divisao = Numero1 / Numero2
print(f'Os números escolhidos foram {Numero1} e {Numero2}. E esses são os resultados: Soma = {soma}, Subtração = {subtracao}, Multiplicação = {multiplicacao} e Divisão = {divisao:.2f}')
'''

'''
2. Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.
'''
'''
nascimento = int(input('Informe seu ano de nascimento: '))
idade = 2024 - nascimento
print(f'Este ano você completa {idade} anos')
'''

'''
3. Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.
'''
'''qm = float(input('Quantos quilômetros?'))
metros = qm * 1000
centimetros = qm * 100000
milimetros = qm * 1000000
print(f'{qm:.2f} quilômetro(s) equivale a {metros:.2f} metros, {centimetros:.2f} centímetros e {milimetros:.2f} milímetros')
'''

'''
4. Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.
'''
'''
litros = float(input('Informe a quantidade de litros consumidos: '))
km = float(input('Informe a quantidade de km percorridos: '))
kml = km / litros
print(f'O consumo foi de {kml:.2f} km/litros !')
'''
      
'''
5. Escreva um programa que calcule o tempo de uma viagem.
Faça um comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião=600km/h
● carro=100km/h
● ônibus=80km/h
'''
'''
distancia = int(input('Entre com a distância em Km da viagem: '))
aviao = distancia / 600
carro = distancia / 100
onibus = distancia / 80
print(f'Essa viagem irá demorar {aviao:.1f} horas de avião, {carro:.1f} horas de carro e {onibus:.1f} horas de ônibus.')
'''

'''
6. Solicite ao usuário o peso em kg e a altura em metros.
Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso/(altura x altura)
'''
'''
peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em metros: '))
IMC = peso / (altura * altura)
print(f'O seu IMC é de {IMC:.2f}')
'''

'''
7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''
'''
ganhahora = float(input('Informe o quanto você ganha por hora: '))
horastrabalhadas = int(input('Informe a quantidade de horas trabalhadas no mês: '))
Salario = ganhahora * horastrabalhadas
print(f'Este mês o seu salário bruto será de {Salario:.2f} reais.')
'''

'''
8. Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.
'''
'''
semana1 = int(input('Informe a quantidade de horas que realizou exercicio físico na semana 1: '))
semana2 = int(input('Informe a quantidade de horas que realizou exercicio físico na semana 2: '))
semana3 = int(input('Informe a quantidade de horas que realizou exercicio físico na semana 3: '))
semana4 = int(input('Informe a quantidade de horas que realizou exercicio físico na semana 4: '))
caloriasporhora = (5*60)*(semana1 + semana2 + semana3 + semana4)
print(f'Você perdeu {caloriasporhora} calorias esse mês')
'''

'''
9. Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo também e esto imigrando de área.
Lembrando que para o retorno vamos usar print com as variáveis criadas e este texto é somente um exemplo,
utilizem a criatividade.
'''
'''
Nome = input('Entre com o seu primeiro nome ou apelido: ')
Hobby = input('Qual seu Hobby? ')
Cor = input('Qual sua cor favorita? ')

print(f'Olá {Nome},')
print(f'{Hobby} parece tão divertido!')
print(f'A cor {Cor} é linda mesmo. Arrasou!')
'''