+++
title = "Utilizando dicionários em Python: uma alternativa ao switch case."
author = "Ariel Fernandes"
date = "2022-09-29"
draft = false
tags = ["Dict"]
type = "posts"
bookCollapseSection = true
+++

Em Python, um dicionário é uma coleção de pares chave-valor, onde cada chave é única e mapeia para um valor específico. É semelhante a uma tabela hash em outras linguagens de programação.

Uma vantagem de se utilizar dicionários em Python é que eles permitem a busca e acesso aos valores armazenados de forma rápida e eficiente, em comparação com o uso de estruturas de controle como o switch case.

Para ilustrar essa ideia, vamos supor que temos uma função que recebe como parâmetro uma string contendo um nome de um mês, e precisamos retornar o número correspondente a esse mês. Em outras linguagens, poderíamos utilizar um switch case para resolver esse problema. Em Python, uma abordagem mais simples e elegante seria utilizar um dicionário:

```python
def obter_numero_do_mes(mes):
    numeros = {
        'janeiro': 1,
        'fevereiro': 2,
        'março': 3,
        'abril': 4,
        'maio': 5,
        'junho': 6,
        'julho': 7,
        'agosto': 8,
        'setembro': 9,
        'outubro': 10,
        'novembro': 11,
        'dezembro': 12
    }
    return numeros.get(mes.lower(), -1)
```

Nesse exemplo, definimos um dicionário chamado numeros, onde cada chave é um nome de mês e o valor correspondente é o número desse mês. Em seguida, utilizamos o método get() do dicionário para obter o valor correspondente à chave passada como parâmetro. O segundo parâmetro do método get() é opcional e é o valor a ser retornado caso a chave não exista no dicionário. No nosso caso, se o valor da chave mes não existir no dicionário, retornamos -1.

O Python também introduziu recentemente uma nova estrutura de controle chamada match case, que é semelhante ao switch case, mas mais expressiva e flexível. A partir da versão 3.10 do Python, podemos utilizar o match case para substituir o dicionário do exemplo anterior:

```python
def obter_numero_do_mes(mes):
    return match(mes.lower()):
        case 'janeiro':
            return 1
        case 'fevereiro':
            return 2
        case 'março':
            return 3
        case 'abril':
            return 4
        case 'maio':
            return 5
        case 'junho':
            return 6
        case 'julho':
            return 7
        case 'agosto':
            return 8
        case 'setembro':
            return 9
        case 'outubro':
            return 10
        case 'novembro':
            return 11
        case 'dezembro':
            return 12
        case _:
            return -1

```
Nesse exemplo, utilizamos a estrutura match case para realizar a mesma tarefa que o dicionário. O valor da variável mes é comparado com cada um dos padrões definidos nos casos, e a ação correspondente é executada quando um padrão corresponde. O caso _ é um caso padrão, que é executado quando nenhum dos outros casos é correspondido. Note que, ao contrário do dicionário, o match case suporta apenas valores simples como padrões (por exemplo, inteiros, strings, etc.) e não suporta operadores complexos ou funções de comparação personalizadas.

Em resumo, o dicionário é uma estrutura de dados poderosa em Python que permite mapear chaves para valores e é uma alternativa mais eficiente e legível ao switch case em muitos casos. O match case é uma nova funcionalidade em Python 3.10 que oferece recursos semelhantes ao switch case, mas ainda não está disponível em versões anteriores.
