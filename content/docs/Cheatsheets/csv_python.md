---
title : Manipulação de CSV em Python
author : Ariel Fernandes
date : 2025-03-13
draft : false
tags : ["csv_python"]
type : posts
---

## 1. Ler um Arquivo CSV
Para ler um arquivo CSV linha por linha, use a biblioteca nativa `csv`. Cada linha será retornada como uma lista.

```python
import csv

# Abre o arquivo CSV em modo de leitura
with open('arquivo.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)  # Cria um objeto leitor
    for row in reader:
        print(row)  # Cada 'row' é uma lista representando uma linha do CSV
```

**Exemplo de Saída**:
Se o arquivo `arquivo.csv` contiver:
```
Nome,Idade,Cidade
Alice,25,São Paulo
Bob,30,Rio de Janeiro
```

A saída será:
```
['Nome', 'Idade', 'Cidade']
['Alice', '25', 'São Paulo']
['Bob', '30', 'Rio de Janeiro']
```

---

## 2. Ler CSV como Dicionário
Para facilitar o acesso às colunas pelo nome, use `csv.DictReader`. Cada linha será retornada como um dicionário, onde as chaves são os cabeçalhos do CSV.

```python
import csv

# Abre o arquivo CSV em modo de leitura
with open('arquivo.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  # Cria um objeto leitor de dicionário
    for row in reader:
        print(row['Nome'], row['Idade'])  # Acessa colunas pelo nome
```

**Exemplo de Saída**:
Com o mesmo arquivo `arquivo.csv`, a saída será:
```
Alice 25
Bob 30
```

---

## 3. Escrever em um CSV
Para criar ou escrever dados em um arquivo CSV, use `csv.writer`.

```python
import csv

# Dados a serem escritos no CSV
dados = [['Nome', 'Idade'], ['Alice', 25], ['Bob', 30]]

# Abre o arquivo CSV em modo de escrita
with open('arquivo.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)  # Cria um objeto escritor
    writer.writerows(dados)  # Escreve todas as linhas
```

**Resultado no Arquivo**:
O arquivo `arquivo.csv` conterá:
```
Nome,Idade
Alice,25
Bob,30
```

---

## 4. Usar Pandas para Ler CSV
A biblioteca `pandas` oferece uma maneira poderosa e simples de trabalhar com arquivos CSV.

```python
import pandas as pd

# Lê o arquivo CSV e cria um DataFrame
df = pd.read_csv('arquivo.csv')
print(df)  # Exibe o DataFrame
```

**Exemplo de Saída**:
Com o mesmo arquivo `arquivo.csv`, a saída será:
```
    Nome  Idade        Cidade
0  Alice     25     São Paulo
1    Bob     30  Rio de Janeiro
```

---

## 5. Filtrar Dados com Pandas
Você pode filtrar dados facilmente usando condições no DataFrame.

```python
import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('arquivo.csv')

# Filtra pessoas com idade maior que 25
filtro = df[df['Idade'] > 25]
print(filtro)

# Salva o resultado filtrado em um novo CSV
filtro.to_csv('resultado_filtrado.csv', index=False)
```

**Exemplo de Saída**:
```
   Nome  Idade         Cidade
1   Bob     30  Rio de Janeiro
```

---

## 6. Configurações Avançadas no Pandas
Use parâmetros adicionais para lidar com separadores personalizados, codificações ou ausência de cabeçalhos.

```python
import pandas as pd

# Lê um CSV com separador ';' e sem cabeçalho
df = pd.read_csv('arquivo.csv', sep=';', header=None, encoding='latin1')
print(df)
```

---

## 7. Adicionar uma Nova Coluna
Adicione novas colunas ao DataFrame para manipular os dados.

```python
import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('arquivo.csv')

# Adiciona uma nova coluna (ex.: dobra a idade)
df['DobroIdade'] = df['Idade'] * 2
print(df)
```

**Exemplo de Saída**:
```
    Nome  Idade        Cidade  DobroIdade
0  Alice     25     São Paulo          50
1    Bob     30  Rio de Janeiro         60
```

---

## 8. Salvar DataFrame como CSV
Salve um DataFrame modificado em um novo arquivo CSV.

```python
import pandas as pd

# Cria um DataFrame
dados = {'Nome': ['Alice', 'Bob'], 'Idade': [25, 30]}
df = pd.DataFrame(dados)

# Salva o DataFrame como CSV
df.to_csv('arquivo_saida.csv', index=False)
```

---

### **Como Usar Este Shortcode**
1. Copie os trechos de código acima e cole-os diretamente no seu projeto Python.
2. Substitua `'arquivo.csv'` pelo caminho do seu arquivo CSV.
3. Altere os nomes das colunas (`'Nome'`, `'Idade'`, etc.) conforme o seu arquivo.

Este shortcode foi projetado para ser prático e fácil de usar, ideal para manipular arquivos CSV rapidamente em Python. 😊
```

---

