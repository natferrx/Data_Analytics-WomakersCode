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

### Módulo, Namespaces, Pacotes e Escopos

Módulo  
São locais onde você define os nomes e funções que quer que fiquem visíveis para o resto do sistema  
É a caixinha, o arquivo!

Namespaces  
Local de definição de nomes.  
É o conteudo dentro do módulo

Na pratica é possível criar um módulo (um arquivo .py) que posso reutilizar em outro arquivo.  
Para utilizar um módulo em outro arquivo, utilizamos o "import" + nome_do_modulo. 

Exemplo:

funcoes_de_log.py

```python
nome_de_usuario = "Dori"

def imprimir_no_log(texto):
    print(f'{texto}')
```

import.py

```python
import funcoes_de_log

funcoes_de_log.imprimir_no_log(f'Bem vinda, {funcoes_do_log.nome_de_usuaria}')
```

Para não precisar ficar colocando o nome_do_modulo.nome_do_namespace() é possível importar da seguinte maneira:

```python
from funcoes_do_log import nome_de_usuario, imprimir_no_log
```
Dessa forma já informamos qual namespace queremos importar e não precisamos mais chamar o nome do módulo ao longo do código. É possível utilzar * para importar todos os namespaces daquele módulo, mas não é considerado boa prática devido a performance caso não utlilite tudo.



### Pacotes

* Existem muitos módulos prontos, como o datetime, que retorna a hora de agora.

Estes módulos ficam dentro de Pacotes (ou também chamado de Bibliotecas). Um exemplo famoso é o Pandas e o Numpy. Esses pacote já contem vários módulos prontos de análise de dados!

python package index  
É um ótimo lugar para consultar bibliotecas de Python.

* Como utilizar um pacote?

pip install  
instalar um pacote individualmente  
Ps.: Deve ser utilizado no terminal e não no código.

pip install -r requirements.txt
instalar uma lista de pacotes

import

exemplo:  
(no terminal) pip install colorama  
(no início do código) import colorama

### Escopo

variáveis locais  
variáriaveis declaradas dentro de uma função, não podem ser acessadas de fora dela, spo existe dentro do escopo.

variais globais  
variáveis declaradas fora de qualquer função, elas se encontram em um escopo que é acessível em qualquer parte do seu script e também por outro módulos.

Se quisermos alterar uma variável global

### Classes e Objetos

#### Programação orientada a objetos (POO)
É um paradigma de programação que modela os dados e comportamentos como se fossem objetos do mundo real.
Objetos possuem em geral dois componentes:
- Propriedades  
Exemplo: Ligado/desligado, canal, volume máximo e mínimo
- Comportamentos  
Exemplo: mudar canal, volume para cima/baixo, ligar/desligar.

```python
televisao.ligar()
televisao.mudar_canal_para_cima()
televisao.aumentar_volume()
```

POO traz novos conceitos para a linguagem:  
classes, heranças, encapsulamento, abstrações e polimorfismo.

#### Classes (class)
 
Classes descrevem o que um objeto vai ser, mas elas não criam o objeto.

- Toda classe tem um método especial chamado construtor.  
O método especial __init__ será chamado sempre que criamos um novo objeto do tipo da classe.

- Método são funções definidas dentro da classe.

- O primeiro parâmetro do método é chamado self e representa a instância sobre a qual o método atuará. Utiliza o self para definir propriedades do próprio objeto.

#### Encapsulamento

Por padrão os atributos e métodos das classes são publicos. Por isso, para indicar quais atributos e mpetodos não deve alterar na classe, nós utilizamos convenções em seus nomes.  
Existem duas convenções para iniciar nomes de métodos e atributos em Python:

- _ (underscore), nomes iniciados por "_" são protegidos e não devem ser acessados pelo mundo externo a não ser que o usuário saiba exatamente o que está fazendo, ou seja, ainda pode existir algum caso de uso.
- __ (underscore duplo), nomes iniciados por "__" são privados e não devem ser acessados pelo mundo externo de forma nenhuma. 

#### Propriedades

Dão acessos a variáveis que se parecem com atributos, mas na verdade usam métodos pór trás dos planos. Eles podem ser usados para reforçar a privacidade das classes.  
Utilizamos um "@"  para definir uma propriedade.


