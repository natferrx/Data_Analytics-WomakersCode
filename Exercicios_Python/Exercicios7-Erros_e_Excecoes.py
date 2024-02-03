# PRATICA 7 - Erros e Exceções (Debuging)
'''
1. O programa abaixo deve calcular a média dos valores digitados
pelo usuário.
No entanto, ele não está funcionando bem. Você pode
consertá-lo?
'''

# PROGRAMA ORIGINAL COM FALHAS

'''
def calcular_media(valores):
    tamanho = 1
    soma = 0.0
    for i, valor in enumerate(valores):
        soma += valor
        i += 1
    media = soma / tamanho

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = false

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))

'''

# PROGRAMA APÓS CORREÇÃO UTILIZANDO O "RUN AND DEBUG" DO VSCODE

def calcular_media(valores):
    tamanho = len(valores)
    soma = 0.0
    for i, valor in enumerate(valores):
        soma += float(valor)
        i += 1
    media = soma / tamanho
    print('A média calculada para os valores {} foi de {}'.format(valores, media))


continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = False
    else:
        valores.append(valor)

calcular_media(valores)
