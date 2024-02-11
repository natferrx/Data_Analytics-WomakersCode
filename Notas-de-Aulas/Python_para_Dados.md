# Python para Dados

## Numpy e o ecossistema Python
Array (tabela, matriz ou tensor) é o objeto principal do Numpy.

- Tabela - Uma dimensão  
- Matriz - 2 dimensões  
- Tensor - 3 dimensões  

### Formas de criar uma array no Numpy

#### Utilizando listas
```python
#Importar a biblioteca Numpy e dar o apelido de np para facilitar a chamada ao longo do código
import numpy as np  

#criar uma lista
l = [4, 8, 2, 12, 5, 8, 0]

#atrubuir a uma array do numpy
arr = np.array(l)

#chamar a lista do numpy
arr
```

#### Criando do zero com comandos

```python
# criar uma array com tamanho 2 por 2 neste exemplo, e preenchida somente com zeros. Primeiro valor smepre vai ser a linha e o segundo valor a coluna.
np.zeros((2,2))

# criar uma array de 1 até 10. Primeiro argumento é o limite inferior, segundo argumento limite superior e o terceiro argumento é o step (incremento) que é opcional, por padrão é 1.
np.arange(1,11)

#criar uma array com números aleatórios de tamanho 3 por 3
np.random.random((3,3))

#criar uma array com números inteiros aleatórios de tamanho 3 linhas por 5 colunas. Primeiro argumento é o limite inferior, segundo argumento é o limite superior e o tamanho com uma tupla.
np.random.randint(10,30, size=(3,5))
```

### Arrays e mais dimensões

#### Array com 3 dimensões (tensor)
![alt text](image.png)
![alt text](image-1.png)

#### shape  
verificar quantas dimensões tem a array

#### flatter  
coloca a array em apenas uma dimensão de uma linha.

#### reshaping  
Muda dimensões. Exemplo, tenho uma array de 2 linhas e 3 colunas, posso pedir para transformar em 3 colunas e 2 linhas com o reshapping.

![alt text](image-2.png)

### Tipos em Numpy

- np.int64
- np.int32
- np.float64
- np.float32
- bool8

#### para conferir o tipo
utilizar o .dtype

#### para converter um tipo
utilizar , dtype=np.int32 ou utilizar o .astype(np.int32)

### Indexação

Sempre começa no zero. E vai até o último index menos 1.
Então se eu tiver uma array de 1 dimensão e quiser os elementos array[2:4], vai ser do segundo elemento até o terceiro elemento.

0 1 2 3 4 5, neste exemplo, iria pegar o 2 e 3.

### FIltragem

#### Mascara (mask)

- Exemplo:

```python
pessoas_id_idade = np.array([[1,22],[2,21],[3,27],[4,26]])

# Filtrando todas as linhas da segunda coluna, estamos conferindo quais valores são divisíveis por 2, ou serja, quais são par
pessoas_id_idade[[:,1]] % 2 == 0
```

array([True, False, False, True])

- Exemplo 2:

```python
arr1 = np.array([1,2,3,4,5])

#Descobrindo quais valores são pares
mask = arr1 % 2 == 0
mask
```

array([False, True, False, True, False])

Exemplo 3:

#Retornar somente as pessoas que tem mais de 21 anos de idade
```python
mask_maior21 = pessoas_id_idade([:,1] > 21)
```


#### Indexação sofisticada (fancy indexing)

Agora, através do Fancy Indexing, posso utilizar a mascara para retornar os valores do array

Exemplo:

```python
arr1[mask]
```

array([2,4])

Exemplo 2:

#retornar quais os valores são maiores que 21 no exemplo 3 de mascaras
```python
pessoas_id_idade[mask_maior21]
```

array([[1, 22], [3, 27], [4,26]])

### Concatenação

#### Concatenar Linhas

```python
np.copncatenate((primeira_array,segunda_array))
```
por padrão é axis=0 (linha)

#### Concatenar Colunas

```python
np.concatenate((primeira_array,segunda_array), axis=1)
```

#### Deletar linhas

```python
np.delete(nome_da_array, 2, axis=0)
```
Neste caso deletaria a terceira linha de uma array

#### Deletar colunas

```python
np.delete(nome_da_array, 1, axis=1)
```
Neste caso deletaria a segunda coluna da array

### Calculo com Array

#### SOMA
- nome_array.sum() -> soma o array inteiro
- nome_array.sum(axis=0) -> soma as linhas, sentido das colunas, o resultado vai ser uma array com quantidas das colunas
- nome_array.sum(axis=1) -> soma as colunas, no sentido das linhas, o resultado vai ter a quantidade de linhas

#### MAX e MIN
- nome_array.min() -> minimo de todo o array
- nome_array.max() -> maximo de todo o array
- nome_array.min(axis=0) -> valor minimo de cada linha
- nome_array.max(axis=1) -> valor maximo de cada coluna

#### MEDIA
- nome_array.mean() -> media de todos os elementos da array
- nome_array.mean(axis=0) -> minimo de cada linha

#### KEEDIMS

Mantem as mesmas dimensões

#### SOMA CUMULATIVA
A cada degrau vai acumulando a soma

nome_array.cumsum(axis=0) -> Soma as linhas de forma cumulativa


### Operação com Vetorização


```python
arr = np.array(["Hello","Meninas","Coders"])
len(arr) > 5
```

Resultado:
False  
Ou seja, retorna se tem mais de 5 elementas na array como um todo

```python
vetorizar_len = np.vetorize(len)
vetorizar_len(arr) > 5
```

Resultado:
array([False, True, True])  
Ou seja, retorna de o cada elemento tem mais de 5 caracteres

### Salvar uma Array em um arquivo

np.save('nome_do_arquivo.npy', nome_da_array)

## Pandas

O Pandas, um pacote Python dedicado à manipulação de dados, também possui funcionalidades para visualização de dados.

Sua estrutura é fundamental em dois pacotes essenciais do Python: Numpy e Matplotlib.

Enquanto o Numpy pferece objetos de matriz multidimensional para facilitar a minipulação de dados, o Matplotlib proporciona ao Pnadas capacidade robusta de visualização de dados.

### Formato de Dados

Tabela, também chamada de dados tabulares (ou dados retangulares).

### Criar um Dataframe

Uma das maneiras é utilizar dicionários e listas.

```python
dados = {
    'Nome': ['Max', 'Bella', 'Rocky', 'Luna'],
    'Raça': ['Labrador', 'Poodle','Boxer','Chihuahua']
}

#Criar o DataFrame

df_cachorros = pd.DataFrame(dados)
```

### Ler arquivos e transformando em DataFrame

#### CSV
```python
df_csv = pd.read_csv('arquivo.csv')
```

#### Excel
```python
df_excel = pd.read_excel('planilha.xlsx', sheet_name='nome_da_planilha')
```
#### Json
```python
df_json = pd.read_json('arquivo.json')
```

#### Parquet
```python
df_parquet = pd.read_parquet('arquivo.parquet')

```
#### SQL
```python
from sqlalchemy import create_engine

engine = create_engine('sqlite://banco_de_dados.db')
query = 'select * from tabela'
df_sql = pd.read_sql(query, engine)
```

### Primeiros métodos de DataFrame

- df.head()  
mostra as primeiras 5 linhas da tabela.

- df.info()  
mostra os nomes das colunas, se tem alguma informação faltando e os tipos daS colunas.

- df.shape  
mostra a quantidade de linhas e de colunas (x,y). Nào precisa usar parentesis é só o "shape" mesmo.

- df.describe()  
mostra contas básicas sobre a tabela, como a média, mediana, contagem, minimo, maximo.

### Componentes do DataFrame

A tabela pandas é como um quebra cabeças com 3 partes:

- values: os valores, que são os dados mesmo.
- columns: as etiquetas (labels) das colunas.
- index: as etiquetas das linhas, id das linhas.

### Ordenação

```python
df.sort_values(`coluna`)
```
Para ordenar uma coluna de forma crescente

```python
df.sort_values(`coluna`, ascending=False)
```
para ordenar de forma decrescente

```python
df.sort_values([`coluna1`,`coluna2`])
```
Para ordenar numtiplas colunas de forma crescente

### Subconjuntos de linhas

```python
df_cachorros[df_cachorros[`Raça`] == `Chihuahua`]
```
Vai filtrar as linha onde a coluna raça seja Chihuahua.


```python
is_marrom_ou_cinza = df_cachorros["Cor"].isin(["Cinza","Marrom"])
df_cachorros[is_marrom_ou_cinza]
```
Para filtrar com base em multiplo valores é interessante utilizar o método ".isin"

### Adicionar uma nova coluna

![alt text](image4.png)

## Agregando Dados

Estatísticas resumidas, como o próprio nome sugere, são números que resumem e fornecem informações sobre seu conjunto de dados.

### Exemplos de funções estatísticas resumidas:

#### .median()
Calcula a mediana de um conjunto de dados, indicando o valor central quando os dados estão ordenados.
#### .mode()
Moda, identifica o(s) valor(es) mais frequente(s) em um conjunto de dados.
#### .min()
Retorna o valor mínimo em um conjunto de dados.
#### .max()
Retorna o valor máximo em um conjunto de dados.

### Medidas de dispersão:

#### .var()
Calcula a variância, uma medida da dispersão dos dados.
#### .std()
Calcula o desvio padrão, indicando a dispersão média dos dados em relação à média.

### Outras funções úteis:

#### .sum()
Soma todos os valores em um conjunto de dados.

#### .quantile()
Calcula um percentil específico em um conjunto de dados, indicando o valor abaixo do qual uma determinada porcentagem dos dados está.

## Estatística Personalizada

O método de agregação (ou agg) permite calcular estatísticas personalizadas.

Exemplo:

```python
def pct50(coluna):
    return coluna.quantile(0.50)

df_cachorros['Altura (cm)'].agg(pct50)
```

resultado 23.0

## Estatística Cumulativa

O Pandas também possui métodos para calcular estatísticas cumulativas.

Chamar "cumsum" em uma coluna não retorna apenas um número, mas um número para cada linha do DataFrame.

Exemplo:

```python
df['Total Vendas Cumulativas'] = df['Vendas'].cumsum()
```

Este código cria uma nova coluna chamada "Total Vendas Cumulativas" que contém o total de vendas cumulativas para cada linha do DataFrame.

Outras funções úteis:

- cumprod(): Calcula o produto cumulativo de uma série.
- cummax(): Encontra o valor máximo cumulativo em uma série.
- cummin(): Encontra o valor mínimo cumulativo em uma série.

## Excluir duplicados

O método drop_duplicates do Pandas remove linhas duplicadas de um DataFrame, permitindo a criação de um novo DataFrame sem repetições com base em critérios específicos definidos pelos valores em determinadas colunas.

O argumento subset especifica as colunas para identificar duplicatas, e o resultado é um DataFrame sem as linhas duplicadas.

Exemplo:

```python
df = df.drop_duplicates(subset=['Coluna1', 'Coluna2'])
```

Este código remove linhas duplicadas do DataFrame df com base nos valores nas colunas 'Coluna1' e 'Coluna2'.

Opções adicionais:

- keep: Especifica se a primeira ou a última linha duplicada deve ser mantida.
- inplace: Modifica o DataFrame original em vez de criar um novo.

## Contagem de Valores Únicos

O método value_counts() do pandas retorna uma contagem de valores únicos em uma coluna de um DataFrame, fornecendo uma série que lista os valores distintos junto com a frequência de cada valor. Isso é útil para entender a distribuição dos dados e identificar os valores mais comuns em uma determinada coluna.

Exemplo:

```python
import pandas as pd

#Criar um DataFrame
df = pd.DataFrame({'coluna': ['A', 'B', 'A', 'C', 'B']})

#Contar os valores únicos na coluna
contagem_valores = df['coluna'].value_counts()

#Exibir a contagem de valores
print(contagem_valores)
```
Saída:

A    2  
B    2  
C    1  


Detalhes adicionais:

- O método value_counts() pode ser usado com colunas de tipo string, inteiro ou float.
- O método retorna uma série Pandas, que é um tipo de dados ordenado que mapeia valores para contagens.
- A série resultante pode ser usada para calcular a frequência de cada valor, a porcentagem de cada valor e a frequência cumulativa de cada valor.
- O método value_counts() também pode ser usado para filtrar um DataFrame por valores específicos.

### método Normalize com value_counts()

Por padrão, o parâmetro normalize está definido como False, o que significa que a série resultante conterá a contagem absoluta de cada valor único.

Se você definir normalize como True, a série resultante conterá a frequência relativa de cada valor único, que é a contagem dividida pelo número total de valores na coluna.

Exemplo:

```python
import pandas as pd

# Criar um DataFrame
df = pd.DataFrame({'coluna': ['A', 'B', 'A', 'C', 'B']})

# Contar os valores únicos na coluna com normalize=False
contagem_valores_absoluta = df['coluna'].value_counts(normalize=False)

# Contar os valores únicos na coluna com normalize=True
contagem_valores_relativa = df['coluna'].value_counts(normalize=True)

# Exibir a contagem de valores
print('Contagem absoluta:')
print(contagem_valores_absoluta)

print('Contagem relativa:')
print(contagem_valores_relativa)
```


Contagem absoluta:  
A    2  
B    2  
C    1  

Contagem relativa:  
A    0.4  
B    0.4  
C    0.2  

Observações:

- A opção normalize=True pode ser útil para comparar a frequência (porcentagem) de valores em colunas com diferentes tamanhos.
- A opção normalize=False pode ser útil para obter a contagem absoluta de valores específicos.

## Agrupamento de Dados

O método groupby() do Pandas é usado para agrupar um DataFrame por uma ou mais colunas, permitindo a aplicação de operações em cada grupo separadamente. 

Ele cria um objeto de grupo que pode ser combinado com várias funções de agregação, como média, soma, mínimo, máximo, entre outras. 

Esse método é frequentemente usado em conjunto com outros métodos, como agg, para calcular estatísticas resumidas para cada grupo de dados.

Exemplo:

```python
import pandas as pd

# Criar um DataFrame
df = pd.DataFrame({'coluna1': ['A', 'B', 'A', 'C', 'B'], 'coluna2': [1, 2, 3, 4, 5]})

# Agrupar o DataFrame pela coluna1
agrupado = df.groupby('coluna1')

# Calcular a média da coluna2 para cada grupo
media_por_grupo = agrupado['coluna2'].mean()

# Exibir a média por grupo
print(media_por_grupo)
```


Saída:

A    2.5  
B    3.5  
C    4.0  

Detalhes adicionais:

- O método groupby() pode ser usado com colunas de tipo string, inteiro ou float.
- O método retorna um objeto groupby, que é um tipo de dados que permite iterar pelos grupos e aplicar funções a cada grupo.
- O objeto groupby pode ser usado com várias funções de agregação, como mean(), sum(), min(), max(), count(), etc.
- O método groupby também pode ser usado para filtrar um DataFrame por valores específicos.

## Tabelas Dinânicas (Pivot Table)

As tabelas dinâmicas são ferramentas poderosas para resumir e analisar grandes conjuntos de dados. Elas permitem que você organize e visualize seus dados de forma eficiente, facilitando a identificação de tendências e padrões.

Noções básicas:

- Uma tabela dinâmica é composta por linhas, colunas e valores.
- As linhas e colunas representam diferentes índices e colunas do DataFrame.
- Os valores representam as medidas que você deseja analisar.


Criando uma tabela dinâmica com Pandas:

- Importe a biblioteca Pandas.
- Carregue seus dados em um DataFrame.
- Utilize a função pivot_table() do Pandas para criar a tabela dinâmica.

Exemplo:

```python
import pandas as pd

# Criar um DataFrame
df = pd.DataFrame({'Data': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
                   'Produto': ['A', 'B', 'A', 'B', 'C'],
                   'Venda': [100, 200, 300, 400, 500]})

# Criar a tabela dinâmica
tabela_dinamica = df.pivot_table(values='Venda', index='Data', columns='Produto', aggfunc=sum)

# Exibir a tabela dinâmica
print(tabela_dinamica)
```

Saída:

Data      A      B      C  
2023-01-01  100   NaN   NaN  
2023-01-02  NaN   200   NaN  
2023-01-03  300   NaN   NaN  
2023-01-04  NaN   400   NaN  
2023-01-05  NaN   NaN   500  

Benefícios:

- As tabelas dinâmicas facilitam a visualização de grandes conjuntos de dados.
- Permitem a rápida identificação de tendências e padrões.
- Permitem a comparação de diferentes categorias de dados.
- Permitem a filtragem e segmentação de dados.

### Substituir valores faltosos

Se definirmos o argumento margins como True, a última linha e a última coluna da tabela dinâmica contêm a média de todos os valores na coluna ou linha, excluindo os valores ausentes que foram preenchidos com zeros.

## Indice e Fatiamento do Dataframe

Usar um index faz o subset mais faceis de se filtrar.

### Alterando Indices

Podemos colocar uma das colunas como índice do Dataframe usando o método set_index

### Removendo o Index

Podemos utilizar o reset_index

### Ordenando o Index

pode-se utiliozar o sort_index()

### Usando loc para acessar e modificar valores em um DataFrame

O método loc do Pandas é uma ferramenta poderosa para acessar e modificar valores específicos em um DataFrame. 

Ele permite que você selecione linhas e colunas por rótulo ou índice, e defina novos valores para as células selecionadas.

Exemplo:

```python
import pandas as pd

# Criar um DataFrame
df = pd.DataFrame({'coluna1': ['A', 'B', 'C', 'D'], 'coluna2': [1, 2, 3, 4]})

# Acessar um único valor
valor = df.loc[1, 'coluna1']

# Modificar um único valor
df.loc[1, 'coluna2'] = 5

# Acessar um conjunto de valores
valores = df.loc[0:2, 'coluna1']

# Modificar um conjunto de valores
df.loc[0:2, 'coluna2'] = [10, 20]

# Exibir o DataFrame
print(df)
```

Saída:

   coluna1  coluna2  
0        A       10  
1        B       20  
2        C        3  
3        D        4  

Detalhes adicionais:

- O método loc pode ser usado para acessar e modificar valores em DataFrames de qualquer tamanho.
- O método loc pode ser usado para selecionar linhas e colunas por nome ou por posição.
- O método loc pode ser usado para definir novos valores para as células selecionadas.

## Gráficos e Valores Faltosos

### Gráficos

A biblioteca básica de visualização de dados é a matplotlib

```python
from matplotlib import pyplot as plt
```

### Lidar com valores faltosos

Em um datafreme do pandas, os valores ausentes são indicados com NaN, que significa Não é um Número. (not a number)

### Detectar valores nulos

isna() é um método que pode ser utilizado para encontrar os valores nulos. Retorna "True" para registros nulos.

any() se usado junto com o isna() ele retorna qual coluna tem algum valor nulo

sum() se usado junto com o isna() ele retorna a quantidade de valores nulos nas colunas

.plot se usada junto com o sum e o isna() você enxerga a quantidade de dados nulos por coluna

### Removendo dados nulos

o método dropna() no pandas é utilizado para remover linhas ou colunas de um dataframe que contenha valores nulos (NaN), facilitando a limpeza e preparação dos dados. Ele pode ser usado para remover linhas com pelo menos um NaN (padrão) ou colunas específicas, proporcionando flexibilidade na manipulação de conjuntos de dados.

### Substituindo Valores Nulos

O método fillna() no pandas é utilizado para preencher valores nulos (NaN) em um DataFrame com valores específicos. Ele oferece a capacidade de substituir os valores ausenter por um número constante, pela média, moda, mediana; ou utilizar lógicas mais avançadas, proporcionando flexibilidade na manipulação de dados faltantes.

Uma boa prática é utilizar junto com o método o "numeric_only = true" para garantir que essa substituição não dê erros no futuro.

# Data Wrangling com Python

Pode ser traduzido como Manipulação de dados ou Tratamento de Dados. TRata-se de preparar os dados para que possam ser facilmente explorados e analisados.