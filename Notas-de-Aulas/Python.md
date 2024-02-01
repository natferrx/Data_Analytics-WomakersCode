# PYTHON

## Comentários

1 linha -> Utilizar # texto

Várias Linhas -> Utilizar 3 aspas simples no inicio e final do comentário: ''' texto '''

## Operações Matemáricas

soma +  
subtração -  
divisão /  
divisão inteira //  
multiplicação *  
igual ==  
maior >  
maior ou igual >=  
menor <  
menor ou igual <=  
resto %  
incremento +=  
decremento -=  

## Tipos

int - Numeros Inteiros  
float - Numeros decimais  
string - Texto  
boll - Booleano, verdadeiro ou falso  

## Principais Comandos

input('texto')  
Solicitar entrada de dados pelo usuário

print("texto")  
Imprimir algo na tela

f'texto {variavel} texto'   
Formatar um texto com uso de variavel

f'texto {variavel:.2f}   
Formatar uma variavel com 2 casas decimais

\n  
quebra linha

## Tomada de Decisão e Estruturas de Repetição

If e Else -> Se uma condição é verdadeira execute X comando, se nao execute Y comando

While -> Enquanto uma condição é verdadeira execute X comando

For -> Para cada condição verdadeira, execute X comando

## Listas, tuplas e dicionários

### Listas   
Definida uma lista abrindo e fechando colchetes. []  
lista = ["maça", "banana", "ovo"]  
lista2 = [3, 6, 9]

.append  
adicionar um item em uma lista  
lista.append('leite')

### Tuplas
As tuplas são lista que não podem ter os valores modificados.  
Definida uma tupla abrindo e fechando parênteses. () 

### Dicionários
Definido um dicionário abrindo e fechando chaves. {}  
Composto de chave e valor.

dicionário = {'Chave':'Valor'}
  
dicionario = {}  
dicionario['maçã'] = 'É uma fruta'  
dicionario['carro'] = 'É um veículo'  

## Funções
Grupo de instruções relacionadas ue executa uma tarefa.

Declaração  
def nome_funcao():

Chamar função  
nome_funcao()

Parâmetros  
def nome_funcao(num1, num2):  
nome_funcao(num1, num2)  
Sempre que utilizamos um parâmetro na chamada da função, precisamos colocar da definição da função também.

## Manipulação de Arquivos  

file = 'arquivo.txt'

### Abertura de Arquivo - Open  
#abertura de arquivo para leitura  
arquivo_leitura = open(file, "r") 

#abertura de arquivo para escrita  
arquivo_escrita = open(file, "w") 

#abertura de arquivos binario  
arquivo_binario = open(file, "wb") 

### Escrever Arquivos - Write

#abertura de arquivo para escrita  
arquivo_escrita = open(file, "w")  
#escrita no arquivo  
arquivo_escrita.write("Texto a ser escrito")  
#fechar o arquivo  
arquivo_escrita.close()

### Ler Conteúdos de Arquivos - Read

#abertura de arquivo para leitura  
arquivo_leitura = open(file, "r")  
#leitura  
leitura = arquivo_leitura.read()  
#fechar o arquivo  
arquivo_leitura.close()  
#Ver as informações  
print(leitura)

## Tratamento de Exceções

try:  

except

Exemplos de except mais comuns:  
- divisão por zero (ZeroDivisionError)
```python
try:  
    resultado = 10/0  
    print(resultado)  
except ZeroDivisionError:  
    print("Erro!") 
else:
    print('sem exceções') 
```

- Tipo de dados, calculo com string, por exemplo (TypeError)


## Métodos Conhecidos

### BUBBLE SORT   
Método utilizado para ordenar números.   

```python
if numero1 > numero2:  
    numero1, numero2 = numero2, numero1  
if numero2 > numero3:  
    numero2, numero3 = numero3, numero2  
if numero1 > numero2:  
    numero1, numero2 = numero2, numero1  
```

Aqui, o código usa condicionais if para comparar os números e trocar suas posições se necessário. Vamos entender o que está acontecendo:  

O primeiro if compara numero1 e numero2. Se numero1 for maior que numero2, as variáveis são trocadas de posição usando a técnica do "swap" (numero1, numero2 = numero2, numero1).  

O segundo if compara numero2 e numero3. Se numero2 for maior que numero3, as variáveis são trocadas de posição (numero2, numero3 = numero3, numero2).  

O terceiro if é usado novamente para garantir que numero1 seja menor ou igual a numero2 após as trocas.  

Esse processo é inspirado no algoritmo de bubble sort, onde as comparações e trocas são feitas até que a lista esteja ordenada.  

## Orientação a Objetos


