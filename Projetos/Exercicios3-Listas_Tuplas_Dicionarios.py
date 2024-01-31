#PRÁTICA 3 - Listas, Tuplas e Dicionários

'''
1. Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões, ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice", e 5 como "Assassino". 
Caso contrário, ela será classificada como "Inocente".
'''
'''
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

for pergunta in perguntas:
    resposta = input(f"{pergunta} (sim/não) ").lower()
    respostas.append(resposta)

respostas_positivas = respostas.count("sim")

if respostas_positivas == 2:
    print("Classificação: Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Classificação: Cúmplice")
elif respostas_positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")
'''

'''
2. Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
'''
'''
# Inicializando uma lista para armazenar as médias
medias_alunos = []

# Solicitando as notas e calculando a média para cada aluno
for i in range(5):  # Loop para cada aluno
    notas = []  # Lista para armazenar as quatro notas
    for j in range(4):  # Loop para cada nota
        nota = float(input(f"Digite a nota {j + 1} do aluno {i + 1}: "))
        notas.append(nota)

    # Calculando a média e armazenando na lista de médias
    media = sum(notas) / 4
    medias_alunos.append(media)

# Contando o número de alunos com média maior ou igual a 7.0
alunos_aprovados = sum(media >= 7.0 for media in medias_alunos)

# Exibindo o resultado
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
'''

'''
3. Crie um dicionário representando um carrinho de compras. 
Adicione produtos (chaves) e quantidades (valores) ao carrinho. Calcule o total do carrinho de compra.
'''
'''
# Inicializando o carrinho de compras como um dicionário vazio
carrinho_de_compras = {}

# Adicionando produtos e quantidades ao carrinho
carrinho_de_compras["produto1"] = 2  # Exemplo: 2 unidades do "produto1"
carrinho_de_compras["produto2"] = 3  # Exemplo: 3 unidades do "produto2"
carrinho_de_compras["produto3"] = 1  # Exemplo: 1 unidade do "produto3"

# Definindo preços dos produtos (poderiam vir de uma base de dados externa)
precos = {"produto1": 10.99, "produto2": 5.99, "produto3": 7.50}

# Calculando o total do carrinho de compras
total = sum(carrinho_de_compras[produto] * precos[produto] for produto in carrinho_de_compras)

# Exibindo o carrinho de compras e o total
print("Carrinho de Compras:")
for produto, quantidade in carrinho_de_compras.items():
    print(f"{produto}: {quantidade} unidades")

print(f"\nTotal do Carrinho de Compras: R${total:.2f}")
'''

'''
4. Crie um dicionário representando contatos (nome, telefone). 
Permita ao usuário procurar por um contato pelo nome.
'''
'''
# Inicializando o dicionário de contatos
contatos = {
    "Alice": "123-456-789",
    "Bob": "987-654-321",
    "Charlie": "555-123-456",
    "David": "333-111-999"
}

# Solicitando ao usuário o nome para procurar
nome_procurado = input("Digite o nome do contato que deseja procurar: ")

# Buscando o contato pelo nome
telefone = contatos.get(nome_procurado)

# Exibindo o resultado
if telefone is not None:
    print(f"Telefone de {nome_procurado}: {telefone}")
else:
    print(f"Contato de {nome_procurado} não encontrado.")
'''

'''
5. Crie duas tuplas. Concatene-as para formar uma nova tupla.
'''
'''
# Criando duas tuplas
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')

# Concatenando as tuplas para formar uma nova tupla
nova_tupla = tupla1 + tupla2

# Exibindo as tuplas originais e a nova tupla
print("Tupla 1:", tupla1)
print("Tupla 2:", tupla2)
print("Nova Tupla:", nova_tupla)
'''

'''
6. Faça um programa que permita ao usuário digitar seu nome e 
em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. 
Dica: lembre-se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
'''
'''
# Solicitando ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ")

# Convertendo o nome para maiúsculas
nome_maiusculo = nome_usuario.upper()

# Exibindo o nome de trás para frente
nome_invertido = nome_maiusculo[::-1]
print("Nome de trás para frente:", nome_invertido)
'''
