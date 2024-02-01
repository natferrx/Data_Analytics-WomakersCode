#PRATICA 4 - Funções

'''
1. Faça um programa, com uma função que necessite de três argumentos, 
e que forneça a soma desses três argumentos.
'''

def soma(num1,num2,num3):
    resultado = num1 + num2 + num3

num1 = float(input('Forneça o primeiro número: '))
num2 = float(input('Forneça o segundo número: '))
num3 = float(input('Forneça o terceiro número: '))

soma(num1, num2, num3)

'''
2. Reverso do número. Faça uma função que retorne o reverso de um número 
inteiro informado. Por exemplo: 127 -> 721.

3. Escreva um script que pergunta ao usuário se ele deseja 
converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função. Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.

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

5. Crie uma função chamada contar_vogais que recebe uma string como parâmetro. 
Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. 
Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.

6. Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma 
palavra secreta de uma lista predefinida. A palavra secreta será representada por espaços em branco, 
um para cada letra da palavra. O jogador terá um número limitado de 6 tentativas. Em cada tentativa, 
o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada 
nas posições correspondentes. Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. 
Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou 
exceda o número máximo de tentativas. 

Dica: Você precisará importar uma biblioteca para resolver esse exercício.
'''