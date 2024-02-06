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

## FIltragem

### Mascara (mask)

- Exemplo:

```python
pessoas_id_idade = np.array([[1,22],[2,21],[3,27],[4,26]])

# Filtrando todas as linhas da segunda coluna, estamos conferindo quais valores são divisíveis por 2, ou serja, quais são par
pessoas_id_idade[:,1]] % 2 == 0
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


### Indexação sofisticada (fancy indexing)

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

