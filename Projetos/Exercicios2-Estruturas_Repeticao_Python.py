#PRÁTICA 2 - Estruturas de Repetição e Tomada de Decisão

'''
1.Faça um Programa que peça dois números e imprima o maior deles.
'''
'''
numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
if numero1 >= numero2:
    print(f'O maior número é {numero1}')
else:
    print(f'O maior número é o {numero2}')
'''

'''
2. Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde! "ou "Boa Noite!" ou "Valor Inválido!",conforme o caso.
'''
'''
turno = input('Qual turno você estuda? Digitar M-matutino ou V-Vespertino ou N-Noturno: ')
if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor Inválido!")
'''

'''
3. Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
'''
nota = -1
while nota>10 or nota<0:
    nota = int(input('Informe uma nota entre 0 e 10: '))
print(f'Nota de {nota} registrada!')
'''

'''
4. Implemente um programa que classifique um aluno com base em sua pontuação em um exame.
O programa deverá solicitar uma nota de 0 a 10. 
Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.
'''
'''
nota = int(input('Informe uma nota entre 0 e 10: '))
if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")
'''

'''
5. Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo 
e classifique-o como equilátero, isósceles ou escaleno.
    equilátero: todos os lados com o mesmo valor.
    isósceles: dois lados com o mesmo valor. 
    escaleno: todos os lados com medidas distintas.
'''
'''
lado1 = float(input('Entre com o valor do primeiro lado do triangulo em mm: '))
lado2 = float(input('Entre com o valor do segundo lado do triangulo em mm: '))
lado3 = float(input('Entre com o valor do terceiro lado do triangulo em mm: '))
if lado1 == lado2 == lado3:
    tipo = "Equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo = "Isósceles"
else:
    tipo = "Escaleno"
print(f"O triângulo é classificado como {tipo}.")
'''

'''
6. Crie um programa que solicite ao usuário um login e uma senha.
O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.
'''
'''
usuario = input('Usuário: ')
senha = input('Senha: ')
if usuario == "admin" and senha == "admin123":
    print("Login efetuado com sucesso!")
else:
    print('Usuário ou senha incorreta!')
'''

'''
7. Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente,
adulto ou idoso.
'''
'''
idade = int(input('Informe a sua idade: '))
if idade < 12:
    resultado = "criança"
elif idade <18:
    resultado = "adolescente"
elif idade < 50:
    resultado = "adulto"
else:
    resultado = "idoso"
print(resultado)
'''

'''
8. Criar um programa em Python que solicite três números ao usuário, 
utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado.
'''
'''
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
if numero1 > numero2 and numero1 > numero3:
    maior_numero = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior_numero = numero2
else:
    maior_numero = numero3
print(f"O maior número entre {numero1}, {numero2} e {numero3} é: {maior_numero}")
'''

'''
9. O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. 
O processo de leitura deve ser encerrado quando o usuário informar o valor zero.
Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados
na contagem e cálculos.
'''
'''
numero = 1
while numero > 0:
    numero = int(input('Digite um número positivo: '))
    if numero < 0:
        print('Atenção! digite numeros positivos.')
        numero = 1
    elif numero == 0:
        print('Saindo do looping!')
        numero = 0
    elif numero > 0:
        if numero % 2 == 0:
            print('Par!')
        else:
            print('Ímpar!')
    else:
        print("Erro!")
        numero = 1
'''

'''
10. Faça um programa que lê três números inteiros e os mostra em ordem crescente.
'''
'''
numero1 = int(input('Informe o numero 1: '))
numero2 = int(input('Informe o numero 2: '))
numero3 = int(input('Informe o numero 3: '))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1
if numero2 > numero3:
    numero2, numero3 = numero3, numero2
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
print("Números em ordem crescente:", numero1, numero2, numero3)
'''

'''
11. Escreva um programa que calcule o salário líquido.
Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
    ● Renda até R$1.903,98: isento de imposto de renda;
    ● Renda entre R$1.903,99 e R$2.826,65: alíquota de 7,5%;
    ● Renda entre R$2.826,66 e R$3.751,05: alíquota de 15%;
    ● Renda entre R$3.751,06 e R$4.664,68: alíquota de 22,5%;
    ● Renda acima de R$4.664,68: alíquota máxima de 27,5%.
'''
'''
salario_bruto = float(input("Digite o salário bruto: "))
if salario_bruto <= 1903.98:
    percentual_ir = 0
elif salario_bruto <= 2826.65:
    percentual_ir = 7.5
elif salario_bruto <= 3751.05:
    percentual_ir = 15
elif salario_bruto <= 4664.68:
    percentual_ir = 22.5
else:
    percentual_ir = 27.5

desconto_ir = (percentual_ir / 100) * salario_bruto

salario_liquido = salario_bruto - desconto_ir

print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Desconto do Imposto de Renda: R${desconto_ir:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")
'''