+++
title = "Introdução a listas e arrays em Python"
author = "Ariel Fernandes"
date = "2023-04-12"
draft = false
tags = ["lista_array_python"]
type = "posts"
bookCollapseSection = true
+++


### Lista

Listas são estruturas mutáveis, o que significa que é possível substituir, inserir ou remover elementos contidos nelas. No entanto, é importante destacar que as listas retornadas pelos operadores de fatia e concatenação são novas listas e não partes da lista original.

O tipo "list" inclui vários métodos chamados mutadores, cujo objetivo é modificar a estrutura de uma lista. Entre os métodos mais utilizados estão o "append", "insert", "pop", "remove" e "sort".

Um exemplo prático do uso desses métodos seria o seguinte:

```
# Criando uma lista vazia
frutas = []

# Adicionando elementos com o método append
frutas.append("maçã")
frutas.append("banana")
frutas.append("abacaxi")
print(frutas) # ['maçã', 'banana', 'abacaxi']

# Inserindo um elemento em uma posição específica com o método insert
frutas.insert(1, "laranja")
print(frutas) # ['maçã', 'laranja', 'banana', 'abacaxi']

# Removendo um elemento com o método remove
frutas.remove("banana")
print(frutas) # ['maçã', 'laranja', 'abacaxi']

# Removendo e retornando o último elemento com o método pop
fruta_removida = frutas.pop()
print(frutas) # ['maçã', 'laranja']
print(fruta_removida) # 'abacaxi'

# Ordenando a lista com o método sort
frutas.sort()
print(frutas) # ['laranja', 'maçã']

```

Observe que esses métodos modificam a lista original, por isso é importante ter cuidado ao utilizá-los.

Os métodos "split" e "join" de strings são muito úteis para manipular textos em Python. O método "split" é usado para dividir uma string em uma lista de palavras com base em um determinado separador. Já o método "join" é usado para unir uma lista de palavras em uma única string, utilizando um separador específico entre elas.

Por exemplo:

```python

# Usando o método split
frase = "O rato roeu a roupa do rei de Roma"
palavras = frase.split()
print(palavras) # ['O', 'rato', 'roeu', 'a', 'roupa', 'do', 'rei', 'de', 'Roma']

# Usando o método join
palavras = ['O', 'rato', 'roeu', 'a', 'roupa', 'do', 'rei', 'de', 'Roma']
nova_frase = " ".join(palavras)
print(nova_frase) # 'O rato roeu a roupa do rei de Roma'

```

No exemplo acima, ao usar o método "split" sem passar um separador como argumento, ele divide a frase em uma lista de palavras com base nos espaços em branco. Em seguida, ao usar o método "join" com um espaço em branco como separador, a lista de palavras é unida novamente em uma única string.

Podemos observar que uma lista, possui métodos bem definidos para serem utilizados, facilitando ao programador trabalhar
com varios tipos, e formas de manipulação.

Vale lembrar que esses métodos são muito flexíveis e podem ser utilizados de diversas formas para manipular textos em Python.

### Array

O array é uma estrutura de dados que representa uma sequência de itens acessíveis ou substituíveis em posições de índice específicas. Ao contrário das listas, o array tem um comprimento fixo quando é criado e não permite adicionar ou remover posições. A estrutura subjacente de uma lista Python é um array, que permite acesso e substituição de itens em posições específicas e também examinar seu comprimento e obter sua representação em string.

O módulo array do Python possui uma classe array que se comporta como uma lista, mas é limitada a armazenar apenas números. Para criar uma nova estrutura de dados que possa armazenar diferentes tipos de dados, podemos usar uma lista Python para isso. A classe Array tem funcionalidades que permitem usar operações comuns como [], len, str e loop for com objetos de array. É importante lembrar que o programador deve definir o tamanho físico ou a capacidade do Array quando ele é criado e o valor padrão para preenchimento é "None".

```python

| Operações Array usuário | Método na classe Array               |
|-------------------------|--------------------------------------|
| a = Array(10)           | __init__(capacity, fillValue = None) |
| len(a)                  | __len__()                            |
| str(a)                  | __str__()                            |
| para o item em a:       | __iter__()                           |
| a[index]                | __getitem__(index)                   |
| a[index] = new_item     | __setitem__(index, new_item)         |

```

Quando uma operação é realizada em um objeto Array, o Python chama automaticamente o método correspondente. Por exemplo, ao percorrer um objeto Array com um loop for, o Python chamará automaticamente o método iter do objeto Array.

Abaixo está o código para implementar a classe Array e uma interação com o shell para demonstrar seu uso. Após criar e testar a classe Array, é importante lembrar que sua utilização é mais restrita do que uma lista e exige uma abordagem diferente ao usá-la.

```python 

class Array:
    """Representa uma array."""

    def __init__(self, capacity, fillValue=None):
        """Capacidade é o tamanho estático do array. fillValue é colocado em cada posição."""
        self.items = [fillValue] * capacity

    def __len__(self):
        """A capacidade do array."""
        return len(self.items)

    def __str__(self):
        """A representação de string do array."""
        return str(self.items)

    def __iter__(self):
        """Suporta o percurso com um laço for."""
        return iter(self.items)

    def __getitem__(self, index):
        """Operador de subscrito para acesso no índice."""
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Operador de subscrito para substituição no índice."""
        self.items[index] = newItem

```

Agora podemos chamar nossa classe Array:

```python
from arrays import Array

a = Array(5)                         # Instância um array com 5 posições

len(a)                               # Apresenta o número de posições

print(a)                             # Mostra o contéudo no array
>>> [None, None, None, None, None]

for i in range(len(a)):              # Substitui o contéudo do array
    a[i] = i + 1

a[0]                                 # Acessa o item na primeira posição
>>> 1

for item in range(len(a)):           # Percorre o array, para mostrar os valores armazenados
    print(item)
```

Concluímos que, embora mais restritivo, o Array é uma estrutura de dados importante para certos casos de uso em que o tamanho é fixo e não precisa ser alterado posteriormente.



Referência:
Lambert, Kenneth A. Fundamentos de Python: estruturas de dados. Cengage Learning, 2019.
