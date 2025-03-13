---
title: Introdução ao C++
author: Ariel Fernandes
date: 2022-06-12
draft: false
tags: ["introcpp"]
type: posts
---

[<img width=200 src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/ISO_C%2B%2B_Logo.svg/1822px-ISO_C%2B%2B_Logo.svg.png">]()

---

# Estrutura Básica

Para iniciarmos um programa em C++, precisamos importar algumas bibliotecas padrão da linguagem. Normalmente, quando usamos uma IDE de programação, ao criar o arquivo `.cpp` diretamente pela IDE, ela já traz essa estrutura por padrão. No entanto, como vamos iniciar do zero, explicarei como criar essa estrutura, detalhando cada item.

---

## Primeiro Passo

Vamos iniciar nosso programa criando um arquivo de texto com a extensão `.cpp`. Vamos dar o nome para nosso arquivo de `primeiroCodigo.cpp`. O nome do arquivo não deve conter espaços entre as palavras nem acentuação, seguindo boas práticas de nomenclatura.

Após criar o arquivo, abra-o com um editor de texto de sua preferência (eu usarei o Vim para esta introdução, mas sinta-se à vontade para escolher qualquer editor).

Feita a criação e abertura do arquivo, o primeiro passo é importar algumas bibliotecas para o funcionamento do código.

A primeira coisa que precisamos importar é a biblioteca `iostream`, que é essencial para o funcionamento do nosso programa em C++. Ela é a base para tudo o que faremos daqui para frente.

Para importar a biblioteca, usaremos o comando `#include`, que faz a inclusão das bibliotecas no nosso sistema. Seu código deverá ficar assim:

```cpp
#include <iostream>
```

Você pode estar se perguntando o que é esse tal de `iostream`. Ele nada mais é do que um gerenciador de entrada e saída do seu programa (I/O). É com ele que podemos fazer todo o gerenciamento, de forma "automática", do nosso programa. Por exemplo, podemos exibir uma mensagem de saída para o usuário, como "Olá, Mundo!". Claro que suas funcionalidades não se limitam a isso, mas sua principal função é garantir essa interação entre usuário e máquina. Sem ela, seu programa nunca funcionará.

---

## Usando a Biblioteca `std`

Após a importação da nossa biblioteca de entrada e saída (`iostream`), vamos fazer mais uma inclusão ao código: definir o uso da biblioteca `std` (Standard Template Library). Essa biblioteca padronizada oferece ao desenvolvedor um conjunto de classes de uso genérico, facilitando o desenvolvimento.

Por exemplo, sem essa biblioteca, um código simples de saída ficaria assim:

```cpp
std::cout << "Olá, Mundo!";
```

Agora, utilizando a biblioteca, podemos reduzir nossa escrita:

```cpp
cout << "Olá, Mundo!";
```

Dessa forma, conseguimos diminuir as chances de erros no programa, pois evitamos repetições desnecessárias, que podem se tornar cansativas ao longo do tempo.

Agora que já expliquei um pouco sobre sua importância, vamos adicioná-la ao código:

```cpp
#include <iostream>

using namespace std;
```

---

## Criando a Função `main`

Feitas essas inclusões, vamos agora iniciar o programa. Para isso, criaremos uma função chamada `main`, do tipo inteiro (`int`), pois sempre precisamos retornar algo ao sistema. Por padrão, todo programa em C++ deve conter essa estrutura. A função `main` é a principal parte do sistema. Para desenvolver qualquer aplicação, sempre precisaremos iniciá-la. Caso contrário, o programa não funcionará, pois não haverá referência de instância, ou seja, não saberá onde começar ou terminar.

```cpp
#include <iostream>

using namespace std;

int main() {
    return 0;
}
```

Lembre-se de que essa função precisa retornar algo, então adicionamos o comando `return 0;`.

Pronto! Agora você já sabe qual é a estrutura básica de um programa em **C++**.

Se estiver utilizando Linux, poderá rodar o código direto pelo terminal usando o seguinte comando:

```bash
g++ -o nome_para_o_arquivo nome_do_arquivo.cpp
```

O `nome_para_o_arquivo` é o programa que será criado para ser executado, enquanto o `nome_do_arquivo.cpp` é o seu código-fonte.

Depois, execute o programa usando:

```bash
./nome_para_o_arquivo
```

Se você fizer esse procedimento com o arquivo criado nesta introdução, provavelmente não aparecerá nenhuma saída, pois não há nada para ser feito. Apenas estruturamos o projeto no formato de programação em **C++**.

---

## Variáveis

Uma variável é um espaço reservado pelo sistema na memória RAM. Esse espaço é temporário, pois fica alocado nessa parte do hardware. Para acessar essas variáveis, precisamos sempre declará-las no código, informando seu nome e tipo.

Assim como na maioria das linguagens, o **C++** também possui seus tipos de variáveis.

### Tipos de Variáveis em C++

| Tipo                | Tamanho        |
|---------------------|----------------|
| `int` (16 bits)     | 2 bytes        |
| `int` (32 bits)     | 4 bytes        |
| `char`              | 1 byte         |
| `double`            | 8 bytes        |
| `float`             | 4 bytes        |
| `bool`              | 1 byte (true/false) |
| `unsigned short int`| 2 bytes        |
| `short int`         | 2 bytes        |
| `unsigned long int` | 4 bytes        |
| `long int`          | 4 bytes        |
| `unsigned int`      | 4 bytes        |
| `string`            | Variável (texto) |

As variáveis mais comuns para quem está começando são:

- **`int`**: Armazena valores inteiros, como `1`, `2`, `55`, etc.
- **`char`**: Armazena caracteres, como `'a'`, `'b'`, `'c'`, etc.
- **`float`**: Armazena números decimais, como `1.2`, `2.2`, `25.510`, etc.
- **`double`**: Muito parecido com o `float`, mas com maior precisão. Por exemplo, se tivermos um valor como `4.9999999999`, o `float` irá aproximá-lo para `4.5`, enquanto o `double` tentará manter o valor mais próximo ao calculado.
- **`string`**: Armazena textos, como nomes, frases, etc.

Agora que vimos os tipos de variáveis, vamos criar um código para exemplificar o uso de algumas delas.

Crie um novo programa em **C++**, por exemplo, `variaveis.cpp`. Após criar o arquivo, adicione alguns tipos de variáveis:

```cpp
#include <iostream>

using namespace std;

int main() {
    int inteiro;
    char letra;
    double decimal;
    float decimal2;
    bool verdadeiro_false;
    string texto;

    return 0;
}
```

Feito isso, agora precisamos atribuir valores padrão às variáveis. Caso contrário, elas podem ser inicializadas com valores aleatórios (lixo de memória), prejudicando o desenvolvimento. Para evitar erros, sempre atribuiremos valores iniciais:

```cpp
#include <iostream>

using namespace std;

int main() {
    int inteiro = 0;
    char letra = 'c';
    double decimal = 5.2;
    float decimal2 = 5.2;
    bool verdadeiro = true;
    bool falso = false;
    string texto = "Programação em C++";

    return 0;
}
```

A saída deve ser algo como:

```
0
c
5.2
5.2
1
0
Programação em C++
```

Já que informamos os tipos, nomes e valores, vamos imprimir isso para ver o que aparecerá. Para imprimir uma saída, precisamos usar o comando `cout`, como foi utilizado anteriormente. Tente fazer isso sozinho para ver o resultado.

Se você conseguiu, vamos continuar.

Você deve ter percebido que o valor booleano (`bool`) foi impresso na tela como o dígito `1`. Isso ocorre porque `true` corresponde a `1`, e `false` a `0`.

---

## Recebendo Valores Digitados pelo Usuário

Agora iremos receber informações digitadas pelo usuário. Será algo simples, mas muito importante para desenvolver aplicações mais complexas futuramente.

Vamos criar um sistema que solicitará ao usuário o nome, idade, peso e altura.

Utilizando os tipos de variáveis:

- `nome`: Será do tipo `string`.
- `idade`: Será do tipo `int`.
- `peso`: Será do tipo `float`.
- `altura`: Será do tipo `float`.

**Obs:** Comandos de entrada e saída:

```cpp
cout << "Imprime uma mensagem ao usuário";
cin >> Recebe mensagem do usuário;
```

Agora que determinamos os tipos de variáveis que utilizaremos, vamos iniciar o desenvolvimento. Crie seu programa e mãos à obra!

```cpp
#include <iostream>

using namespace std;

int main() {
    string nome;
    int idade = 0;
    float peso = 0.0;
    float altura = 0.0;

    // Agora vamos criar a interação com o usuário
    cout << "Digite seu nome: ";
    cin >> nome;
    cout << "Digite sua idade: ";
    cin >> idade;
    cout << "Digite seu peso: ";
    cin >> peso;
    cout << "Digite sua altura: ";
    cin >> altura;

    return 0;
}
```

Já coletamos as informações. Agora vamos mostrá-las ao usuário. Ainda dentro do seu programa, após toda a coleta de dados, vamos adicionar a saída.

Vamos concatenar as variáveis numa mensagem. Para realizar esse procedimento, é necessário utilizarmos no `cout` nosso comando de saída, o símbolo `<<`, seguido da variável e, opcionalmente, do comando de quebra de linha `endl`.

O `endl` é um comando de quebra de linha. Você pode usar `\n` no lugar dele, que terá o mesmo efeito.

```cpp
// Mostrando os valores inseridos pelo usuário
cout << "Nome: " << nome << endl;
cout << "Idade: " << idade << endl;
cout << "Peso: " << peso << endl;
cout << "Altura: " << altura << endl;
```

Só rodar o seu código, e você verá as mensagens na sua tela.

O código completo deve ficar assim:

```cpp
#include <iostream>

using namespace std;

int main() {
    string nome;
    int idade = 0;
    float peso = 0.0;
    float altura = 0.0;

    // Agora vamos criar a interação com o usuário
    cout << "Digite seu nome: ";
    cin >> nome;
    cout << "Digite sua idade: ";
    cin >> idade;
    cout << "Digite seu peso: ";
    cin >> peso;
    cout << "Digite sua altura: ";
    cin >> altura;

    // Mostrando os valores inseridos pelo usuário
    cout << "Nome: " << nome << endl;
    cout << "Idade: " << idade << endl;
    cout << "Peso: " << peso << endl;
    cout << "Altura: " << altura << endl;

    return 0;
}
```
