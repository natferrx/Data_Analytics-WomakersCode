# Banco de Dados SQL

## Estrutura e arquitetura de dados

### Tipos de Dados

- Estruturados  
São aqueles que seguem um formato padronizado e pré definido, que facilita a manipulação e análise. Exemplos: 
    - Armazenar informações de clientes, produtos ou vendas;
    - Realizar consultas, cálculos ou relatórios;
    - Aplicar algoritmos de aprendizado de máquina.
    
- Não Estruturados  
São aqueles que não seguem um formato específico ou padronizado, e que podem variar em tamanho, tipo e conteúdo. Exemplos:  
    - Extrair sentimentos, tópicos ou entidades de texto;
    - Reconhecer rostos, objetos ou emoções em imagens ou vídeos;
    - Transcrever ou traduzir áudios.

- Semi Estruturados  
São aqueles que possuem algum grau de organização, mas que não se encaixam completemente em um formato rígido ou padronizado. Exemplos:
    - Armazenar e trocar dados entre diferentes sistemas ou aplicações;
    - Integrar dados de diversas fontes ou formatos;
    - Indexar ou pesqusiar dados na web.

### Banco de dados

É um conjunto de dados que podem ser armazenados, acessados, manipulados e analisados de forma eficiente. 

#### Banco de dados relacional

Sua estrutura usa tabelas, com linhas e colunas, para organizar os dados e compreende uma linguagem de programação chamada SQL (Structured Query Language). Cada linha correspon de a um registro ou entidade e cada coluna corresponde a um atributo ou propriedade.

Os bancos de dados relacionais mais conhecidos: SQL Server, SQL do Azure, My SQL, PostgreSQL e MariaDB.

#### Banco de dados não relacionais

São sistemas que armazenam e recuperam dados (semi estruturados ou não estruturados) de forma diferente do modelo relacional tradicional, que usa tabelas, colunas e linhas. O termo NoSQL significa "not only SQL"indicando que esses sistemas podem usar outras formas de consulta além da linguagem padrão SQL.

Banco de dados NoSQL priorizam a disponibilidade e a tolerância a falhas, seguindo as propriedades BASE (basicamente disponíneis, evntualmente consistentes).

Há diferentes tipos de bancos de dados NoSQL cada um com suas próprias características, vantagens e desvantagens Os principais tipos são:

- Banco de dados orientados a documentos
- Banco de dados orientados a grafos
- Banco de dados orientados a chave-valor
- banco de dados orientados a colunas

## SQL

É a principal linguagem de manipulação de banco de dados e uma habilidade essencial para profissionais que lidam com dados.

A linguagem SQL organiza seus comandos em 5 subconjuntos:

- DQL (Data Query Language), são comandos de consulta. OU seja, SELECT.
- DML (Data Manipulation Language), são os comandos que interagem com os dados dentro de tabelas. Ou seja, INSERT, UPDATE e DELETE.
- DDL (Data Definition Languagem), são os comandos que interagem com os objetos do banco. Ou seja, CREATE, ALTER e DROP.
- DCL (Data Control Language), são comandos para controlar a parte de segurança do banco de dados. Ou seja, GRANT e REVOKE.
- DTL (Data Transaction Language ou TCL), são comandos para controle de transação. OU seja, BEGIN, COMMIT e ROLLBACK.

## JOINS

### INNER JOIN
Semelhantes em ambas as tabelas

### LEFT JOIN
Todas as informaçoes da tabela a esquerda e completa com os que existem na direita ou "none" quando nao existir.

### RIGHT JOIN
Todas as informaçoes da tabela a direita e completa com os que existem na esquerda ou "none" quando nao existir.

### FULL JOIN
retorna todasd as informações das duas tabelas, qwuando não tem semelhança retorna "none"

## SUB-CONSULTAS

Conhecida como Sub-queries ou Sub-Select são consultas criadas dentro da consulta principal, então elas permitem usar uma consulta como parte de uma condição de uma outra consulta.




