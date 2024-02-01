#PRATICA 4 - Funções

'''
1. Faça um programa, com uma função que necessite de três argumentos, 
e que forneça a soma desses três argumentos.
'''

'''
def soma(num1,num2,num3):
    resultado = num1 + num2 + num3
    print(resultado)

num1 = float(input('Forneça o primeiro número: '))
num2 = float(input('Forneça o segundo número: '))
num3 = float(input('Forneça o terceiro número: '))

soma(num1, num2, num3)
'''

'''
2. Reverso do número. Faça uma função que retorne o reverso de um número 
inteiro informado. Por exemplo: 127 -> 721.
'''
'''
def reverso(num):
    numero_str = str(num)
    reverso_str = numero_str[::-1]
    reverso_int = int(reverso_str)
    print(f'O número informado foi {num} e seu reverso é {reverso_int}')

num = int(input('Forneça um número inteiro: '))
reverso(num)
'''

'''
3. Escreva um script que pergunta ao usuário se ele deseja 
converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. 
Para cada opção, crie uma função. 
Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, 
onde esse menu chama a função de conversão correta.
'''
'''
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu_conversao():
    print("Escolha a opção de conversão [1 ou 2]:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")

def main():
    menu_conversao()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = celsius_para_fahrenheit(celsius)
        print(f"{celsius} graus Celsius é igual a {resultado:.2f} graus Fahrenheit.")
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit é igual a {resultado:.2f} graus Celsius.")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

main()
'''

'''
4. Crie um programa que leia quanto dinheiro uma pessoa tem 
na carteira e calcule quanto poderia comprar de cada moeda estrangeira. 
Considere a tabela de conversão abaixo:
   - Dólar Americano: R$4,91
   - Peso Argentino: R$0,02
   - Dólar Australiano: R$3,18
   - Dólar Canadense: R$3,64
   - Franco Suíço: R$0,42
   - Euro: R$5,36
   - Libra esterlina: R$6,21
'''
'''
def converter_para_moeda(valor, taxa):
    return valor / taxa

def main():
    # Tabela de conversão
    tabela_conversao = {
        "Dólar Americano": 4.91,
        "Peso Argentino": 0.02,
        "Dólar Australiano": 3.18,
        "Dólar Canadense": 3.64,
        "Franco Suíço": 0.42,
        "Euro": 5.36,
        "Libra esterlina": 6.21
    }

    # Solicitar ao usuário a quantidade de dinheiro na carteira
    dinheiro_carteira = float(input("Digite quanto dinheiro você tem na carteira (em reais): "))

    # Calcular e exibir quanto a pessoa poderia comprar em cada moeda estrangeira
    print("\nQuanto você poderia comprar em cada moeda estrangeira:")
    for moeda, taxa in tabela_conversao.items():
        quantidade_comprada = converter_para_moeda(dinheiro_carteira, taxa)
        print(f"{moeda}: {quantidade_comprada:.2f}")

main()
'''

'''
5. Crie uma função chamada contar_vogais que recebe uma string como parâmetro. 
Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. 
Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.
'''
'''
def contar_vogais(frase):
    # Inicializando o contador de vogais
    contador = 0

    # Iterando sobre cada caractere na frase
    for caractere in frase:
        # Verificando se o caractere é uma vogal (considerando maiúsculas e minúsculas)
        if caractere.lower() in "aeiou":
            contador += 1

    return contador

def main():
    # Solicitando ao usuário que insira uma frase
    frase = input("Digite uma frase: ")

    # Chamando a função contar_vogais
    total_vogais = contar_vogais(frase)

    # Exibindo o resultado
    print(f"A frase '{frase}' possui {total_vogais} vogais.")

main()
'''

'''
6. Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma 
palavra secreta de uma lista predefinida. A palavra secreta será representada por espaços em branco, 
um para cada letra da palavra. O jogador terá um número limitado de 6 tentativas. Em cada tentativa, 
o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada 
nas posições correspondentes. Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. 
Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou 
exceda o número máximo de tentativas. 

Dica: Você precisará importar uma biblioteca para resolver esse exercício.
'''
'''
import random

def escolher_palavra():
    palavras = ["python", "programacao", "desafio", "computador", "tecnologia"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jogar_forca():
    palavra_secreta = escolher_palavra()
    tentativas_maximas = 6
    letras_corretas = []
    letras_incorretas = []

    print("Bem-vindo ao Jogo da Forca!")
    print(mostrar_palavra(palavra_secreta, letras_corretas))

    while tentativas_maximas > 0:
        letra_usuario = input("Digite uma letra: ").lower()

        if letra_usuario.isalpha() and len(letra_usuario) == 1:
            if letra_usuario in letras_corretas or letra_usuario in letras_incorretas:
                print("Você já tentou essa letra. Tente novamente.")
            elif letra_usuario in palavra_secreta:
                letras_corretas.append(letra_usuario)
            else:
                letras_incorretas.append(letra_usuario)
                tentativas_maximas -= 1
        else:
            print("Entrada inválida. Digite apenas uma letra.")

        print("Palavra: ", mostrar_palavra(palavra_secreta, letras_corretas))
        print("Letras incorretas:", letras_incorretas)
        print("Tentativas restantes:", tentativas_maximas)

        if "_" not in mostrar_palavra(palavra_secreta, letras_corretas):
            print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
            break

    if tentativas_maximas == 0:
        print("Você perdeu. A palavra era:", palavra_secreta)

jogar_forca()
'''