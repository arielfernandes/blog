---
title : Regex (Expressões Regulares)
author : Ariel Fernandes
date : 2025-03-13
draft : false
tags : ["regex"]
type : posts
---

## Introdução
As Expressões Regulares (Regex) são padrões usados para combinar sequências de caracteres em strings. Elas são amplamente utilizadas em linguagens de programação, ferramentas de busca e substituição, validação de dados, etc.

---

## Símbolos Básicos

| Símbolo   | Descrição                          | Exemplo               | Matches             |
|-----------|------------------------------------|-----------------------|---------------------|
| `.`       | Qualquer caractere (exceto `\n`)  | `a.b`                 | `aab`, `acb`, `a1b` |
| `\d`      | Dígito (`0-9`)                    | `\d\d`                | `42`, `78`          |
| `\D`      | Não dígito                        | `\D\D`                | `ab`, `@#`          |
| `\w`      | Caractere alfanumérico (`a-z`, `A-Z`, `0-9`, `_`) | `\w\w` | `ab`, `12`, `_Z`    |
| `\W`      | Não alfanumérico                  | `\W\W`                | `!!`, `$$`          |
| `\s`      | Espaço em branco (espaço, tab, nova linha) | `\s`     | ` `, `\t`, `\n`     |
| `\S`      | Não espaço em branco              | `\S\S`                | `ab`, `12`          |

---

## Quantificadores

| Quantificador | Descrição                            | Exemplo         | Matches           |
|---------------|--------------------------------------|-----------------|-------------------|
| `*`           | Zero ou mais ocorrências            | `a*`            | `""`, `a`, `aa`   |
| `+`           | Uma ou mais ocorrências             | `a+`            | `a`, `aa`, `aaa`  |
| `?`           | Zero ou uma ocorrência              | `colou?r`       | `color`, `colour` |
| `{n}`         | Exatamente `n` ocorrências          | `\d{3}`         | `123`, `456`      |
| `{n,}`        | No mínimo `n` ocorrências           | `\d{2,}`        | `12`, `1234`      |
| `{n,m}`       | Entre `n` e `m` ocorrências         | `\d{2,4}`       | `12`, `1234`      |

---

## Âncoras

| Âncora    | Descrição                            | Exemplo         | Matches           |
|-----------|--------------------------------------|-----------------|-------------------|
| `^`       | Início da string                    | `^abc`          | `abc123`          |
| `$`       | Fim da string                       | `xyz$`          | `123xyz`          |
| `\b`      | Limite de palavra                   | `\bword\b`      | `word`, ` word `  |
| `\B`      | Não limite de palavra               | `\Bword\B`      | `swordfish`       |

---

## Classes de Caracteres

| Classe         | Descrição                            | Exemplo         | Matches           |
|----------------|--------------------------------------|-----------------|-------------------|
| `[abc]`        | Qualquer caractere na lista         | `[abc]`         | `a`, `b`, `c`     |
| `[^abc]`       | Qualquer caractere **não** na lista | `[^abc]`        | `d`, `1`, `@`     |
| `[a-z]`        | Intervalo de caracteres             | `[a-z]`         | `a`, `b`, ..., `z`|
| `[0-9]`        | Intervalo de dígitos                | `[0-9]`         | `0`, `1`, ..., `9`|

---

## Grupos e Capturas

| Construção     | Descrição                            | Exemplo         | Matches           |
|----------------|--------------------------------------|-----------------|-------------------|
| `(abc)`        | Grupo de captura                    | `(abc)+`        | `abc`, `abcabc`   |
| `(a|b)`        | Alternativa (OU)                    | `(cat|dog)`     | `cat`, `dog`      |
| `\1`, `\2`     | Referência a grupos capturados      | `(\d)\1`        | `11`, `22`        |
| `(?:abc)`      | Grupo sem captura                   | `(?:abc)+`      | `abc`, `abcabc`   |

---

## Modificadores (Flags)

| Flag      | Descrição                            | Exemplo         | Matches           |
|-----------|--------------------------------------|-----------------|-------------------|
| `i`       | Ignora maiúsculas/minúsculas         | `/abc/i`        | `abc`, `ABC`      |
| `g`       | Global (todas as ocorrências)        | `/abc/g`        | Todas as `abc`    |
| `m`       | Multilinha (`^` e `$` funcionam por linha) | `/^abc/m` | `abc\nabc`        |
| `s`       | Ponto (`.`) inclui quebras de linha  | `/a.c/s`        | `a\nc`            |

---

## Exemplos Práticos

### Validação de Emails
```bash
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```
- Matches: `example@example.com`, `user.name+tag+sorting@gmail.com`

### Validação de Números de Telefone
```bash
^\+?[0-9]{1,3}?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$
```
- Matches: `+1-800-555-5555`, `+55 (11) 98765-4321`

### Extrair URLs
```bash
https?:\/\/[^\s/$.?#].[^\s]*
```
- Matches: `http://example.com`, `https://www.site.com/path`

---

## Ferramentas Úteis

- [Regex101](https://regex101.com/) - Testador interativo de regex com explicações detalhadas.
- [RegExr](https://regexr.com/) - Outro testador interativo com tutoriais.
- [Debuggex](https://www.debuggex.com/) - Visualizador gráfico de regex.

---

## Observações Importantes
- Use `\` para escapar metacaracteres (`\.`, `\+`, etc.) quando precisar deles como literais.
- Sempre teste suas expressões regulares em diferentes cenários para garantir a precisão.
- Regex pode ser poderoso, mas também complexo. Prefira soluções simples sempre que possível.

---
