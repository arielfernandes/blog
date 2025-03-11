+++
title = "Multiplexadores"
author = "Ariel Fernandes"
date = "2022-09-29"
draft = false
tags = ["mux"]
type = "posts"
bookCollapseSection = true
+++

Possui M entradas de dados e uma saída (Mx1), permitindo que apenas uma das entradas seja passada para a saída.
Pode ser chamado de seletor, pois seleciona uma das entradas para à saída.

Multiplexador produz um 1 ou um 0 na saída, dependendo de se a entrada selecionada tem um 1 ou 0.

![](https://raw.githubusercontent.com/arielfernandes/blog/main/resources/_gen/images/mux/selSaida.png)

# Multiplexador 2x1
Tem duas entradas de dados i1 e i0, uma entrada de seleção s0 e uma saída de dados d.

![](https://raw.githubusercontent.com/arielfernandes/blog/main/resources/_gen/images/mux/mux2x1.png)

# Multiplexador 4x1

Quatro entradas de dados i3, i2, i1 e i0, duas entradas de seleção s1 e s0, e uma saída de dados d.

Um multiplexador sempre tem uma saída de dados, não importando quantas entradas
possui.

Ex:. 4x1

Para saber o número de seleções é necessário aplicar log2(x), assim você terá a quantidade de seleção.

Para 4x1, aplicar log2(4) = 2, ou seja este possui duas seleções.

![](https://raw.githubusercontent.com/arielfernandes/blog/main/resources/_gen/images/mux/mux4x1.png)


# Multiplexador Mx1 de N bits

São usados seletivamente para deixar passar não só bits isolados, mas também itens com N bits de dados.

Um conjunto de entradas A pode consistir em quatros bits, a3, a2, a1 e a0, em outro conjunto de entradas b também podem consistir em quatro bits.

Conduzindo o conjunto em uma saída de 4 bits c.


![](https://raw.githubusercontent.com/arielfernandes/blog/main/resources/_gen/images/mux/mux4bitsc.png)

---
Conteúdo retirado do livro Sistemas Digitais, por Frank Vahid.
