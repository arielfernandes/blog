[<img width=200 src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/ISO_C%2B%2B_Logo.svg/1822px-ISO_C%2B%2B_Logo.svg.png">]()

# Introdução ao C++

#### Estrutura básica

Para iniciarmos um progrma em c++, precisamos importar algumas bibliotecas
padrão da linguagem, normalmente quando usamos alguma IDE de programação, quando
criamos o arquivo .cpp direto pela IDE, ela por definição trás essa estrutura.
Mas como vamos iniciar do zero, irei explicar como criar essa estrutura,
explicando cada item.

# Primeiro passo
Vamos iniciar nosso programa criando um arquivo de texto, com a extenção .cpp, vamos dar o nome para nosso arquivo de primeiroCodigo.cpp, seu arquivo não deve conter espaço entre as palavras e nem acentuação, por definicição e boas práticas iremos evitar esse tipo de escrita para nossos programas.

Após criar o arquivo, abra ele com um editor de texto de sua preferência, eu irei usar o vim para essa introdução, sinta-se a vontade para escolher qualquer editor.

Feito a criação e a abertura do nosso arquivo, o primeiro passo é importar algumas biblioteacas para o funcionamento do código.

A primeira coisa que precisamos importar ao código é biblioteca **iostream**, ela é muito importante para o funcionamento do do nosso programa em c++, é a base para tudo que iremos fazer daqui pra frente.

Para importamos a biblioteca iremos utilizar o comando **#include**, no qual faz a importação das bibliotecas dentro do nosso sistema, seu código deverá ficar assim:

```cpp
#include <iostream>

```
Você pode estar se perguntando o que seria esse tal de **iostream**, ele nada mais é do que um gerenciador de entrada e saída do seu programa (**I**|**O**), é com ele que podemos fazer todo o gerenciamento, de forma "automatica", do nosso programa, como por exemplo, uma saida de texto para o usuário informando uma mensagem de "olá". Claro que não se limita só a isso, mas sua principal função é garantir essa interação de usuário e máquina, caso contrário seu programa nunca irá funcionar.

Após a importação da nosso biblioteca de entra e saída (**iostream**), vamos fazer mais uma inclusão ao código, agora iremos definir o uso de uma biblioteca, que é a **std** (Standar Template Library), é uma bibliotexa padronizada de funções, que oferece ao desenvolver um conjunto de classes de uso genérico, facilitando o desenvolvimento.

#### Por exemplo
Sem essa biblioteca, um código simples de saída ficaria assim:

```cpp
std::cout << "Olá Mundo!";
```
Agora utilizando a biblioteca, podemos reduzir nossa escrita:

```cpp

cout << "Olá Mundo!";

```
Dessa forma, conseguirmos diminuir as chances de erros no programa, já que não precisaremos fazer essa inclusões, que se tornam chatas ao longo do tempo.

Agora que já expliquei um pouco sobre sua importância, vamos adiciona-lá ao código.


```cpp
#include <iostream>

using namespace std;
```

Feita essas inclusões, vamos agora iniciar o programa, para isso iremos criar uma função chamada **main**, do tipo inteiro, pois precisamos sempres retornar algo ao sistema, e nesse caso por padrão o programa deve conter essa estrutura. O **main** é a principal parte do seu sistema, para desenvolvermos qualquer aplicação, sempre necessitaremos iniciá-lo, caso isso não seja feito, seu programa não irá funcionar, pois não existe nenhuma referência de instancimento, onde sua estrutura deve começar e terminar.

```cpp
#include <iostream>

using namespace std;

int main() {


}

```

Lembre-se que essa função precisa retornar alguma coisa, então vamos adicionar um **return** no código, essa resposta será zero (return 0):

~~~cpp

#include <iostream>

using namespace std;

int main() {

return 0;
}
~~~

Pronto, agora você já sabe qual é a estrutura básica de um programa em
***c++***. Se você estiver utilizando linux, porderá rodar o código direto pelo
terminal usando o seguindo comando:

```bash
g++ -o nome_para_o_arquivo nome_do_arquivo.cpp
```
O nome_para_o_arquivo é o programa que será criado para ser executado, já o nome_do_arquivo.cpp
é o seu código.

Depois é só executar usando:

~~~bash
./nome_para_o_arquivo

~~~

Se você fizer esse procedimento com o arquivo criado nessa introdução,
provavelmente não aparecer nenhuma saída, pois não há nada para ser feito.
Apenas estruturamos o projeto no formato de programação em ***c++***.

# Variáveis
Uma variável é um espaço separado pelo sistema dentro da memória **RAM**, esse
espaço é temporário, já que fica alocado nessa parte do hardware. Para termos
acesso a essas variáveis precisamos sempre indica-lás dentro do nosso código, o
nome e o tipo dela.

Como na maioria das linguagens o ***cpp*** também contém suas formas de
armazenamento de informações.

#### Os tipos de variáveis em c++

Tipo | Tamanho
---- | ----
int (16bits) | 2 bytes
int (32bits) | 4 bytes
char | 1 byte (caracteres)
double | 8 bytes
float | 4 bytes
bool | 1 byte (true/false)
unsigned shirt int | 2 bytes
short int | 2 bytes
unsigned long int | 4 bytes
long int | 4 bytes
unsigned int (16 bits) | 4 bytes
string | variável (texto)

As variáveis mais comuns de se utilizar quando se inicia em programação, são:

* ***int*** - inteiro
	* armazena valores como, 1, 2, 55 e assim por diante (ou seja somente números).
* ***char*** - caracteres
	* armazena valores como, a, b, c, e assim por diante (ou seja somente letras).
* ***float*** - decimal
	* armazena valores como, 1.2, 2.2, 25.510 e assim por diante (ou seja números com casas decimais).
* ***double*** - decimal
	* Muito parecido com o float, mas possui uma diferença bem importante, o double irá armazenar 
	  valores com mais precisão, se tivermos algum valor que seu resultado seja 4,9999999999, o 
		float irá aproximar o valor,	ficando 4.5, já double tenta manter o valor mais proximo 
		ao calculado.
* ***string*** - Textos
	* armazena valores como, nomes, textos, etc... 

Agora que já vimos os tipos de variáveis, vamos criar um código para exemplificar o uso de algumas delas.<br />
Para isso crie um novo programa ***cpp***, irei chamar o meu de ***variaveis.cpp***, após criar o arquivo, iremos adicionar alguns tipos de variáveis:

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

Feito isto, agora precisamos informar um valor padrão, caso não façamos isso,
sua variável tem o risco de ser iniciada com valores aleátorios, prejudicando seu
desenvolvimento, baśicamente irá iniciar com "LIXO" de memória, para evitarmos
alguns erros, iremos sempre indicar um valor padrão:


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
	string texto = "Programação em cpp";

	
	return 0;

}

```

A saída deverá sair parecida:

```bash
 0
 c
 5.2
 5.2
 1
 0
 Programação

```

Já que informamos os tipos, nomes e valores, vamos imprimir isso para vermos o
que irá aparecer.  Para imprimir alguma saída precisamos usar o comando
***cout***, como foi utilizado anteriormente, tente fazer sozinho, para ver o
resultado.

Se você conseguiu, vamos continuar.

Você deve ter percebido que o valor booleano (bool) foi imprimido na tela com o
digíto um. Isso porque, ***true*** corresponde a um, e ***false*** a zero.


# Recebendo valores digitados pelo usuário

Agora iremos receber algumas informaçãoes digitadas pelo usuário, será algo
simples, mas muito importante para podermos desenvolver aplicações mais
complexas futuramente. 

Vamos criar um sistema que solicitará ao usuário, nome, idade, peso e altura.

Utilizando os tipos de variáveis:
>***nome*** vai ser do tipo string<br />
>***idade*** vai ser do tipo inteiro<br />
>***peso*** vai ser do tipo float<br />
>***altura*** vai ser do tipo float<br />
>Obs: Comando de entrada
> * cout << "Imprime uma mensagem ao usuário";
> * cin >> Recebe mensagem do usuário;

Agora que determinamos os tipos de variáveis que utilizaremos, vamos iniciar o
desenvolvimento, crie seu programa e mão na massa.

```cpp
#include <iostream>

using namespace std;

int main() {
	string nome;
	int idade = 0;
	float peso = 0.0;
	float altura = 0.0;

	//Agora vamos criar a interção com o usuário
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

Já coletamos as informações, agora vamos mostrar elas ao usuário.
Ainda dentro do seu programa, após toda a coleta de dados, vamos adicionar a
saída.

Vamos concatenar as variáveis numa mensagem, é simples, para realizar esse
procedimento é necessario utilizarmos no ***cout*** nosso comando de saída, o
simbolo ***<<*** após a sua resposta, ficará assim:

> cout << "Sua mensagem aqui " << variável aqui << endl;<br />

O ***endl*** é um comando de quebra de linha, você pode utilizar aspas duplas
barra n (**\n**) no lugar dele, terá o mesmo efeito, ou apenas utilizar aspas duplas (" "), porém apenas fechará o código.

```cpp

//mostrando os valores inserido ao usuário
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

	//Agora vamos criar a interção com o usuário
	cout << "Digite seu nome: ";
	cin >> nome;
	cout << "Digite sua idade: ";
	cin >> idade;
	cout << "Digite seu peso: ";
	cin >> peso;
	cout << "Digite sua altura: ";
	cin >> altura;

	//mostrando os valores inserido ao usuário
	cout << "Nome: " << nome << endl;
	cout << "Idade: " << idade << endl;
	cout << "Peso: " << peso << endl;
	cout << "Altura: " << altura << endl;

	return 0;
}

```




