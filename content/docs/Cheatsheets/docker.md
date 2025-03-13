---
title : Docker
author : Ariel Fernandes
date : 2025-03-13
draft : false
tags : ["docker"]
type : posts
---

## Introdução
O Docker é uma plataforma de contêineres que permite criar, implantar e executar aplicativos em ambientes isolados chamados **contêineres**. Este cheatsheet aborda os principais comandos e conceitos do Docker.

---

## 1. Comandos Básicos

| Comando                     | Descrição                                      |
|-----------------------------|------------------------------------------------|
| `docker version`            | Exibe a versão do Docker instalada.           |
| `docker info`               | Mostra informações detalhadas sobre o Docker. |
| `docker --help`             | Exibe ajuda geral do Docker.                  |

---

## 2. Imagens

### Listagem e Gerenciamento

| Comando                     | Descrição                                      |
|-----------------------------|------------------------------------------------|
| `docker images`             | Lista todas as imagens locais.                |
| `docker pull <imagem>`      | Baixa uma imagem do Docker Hub.               |
| `docker rmi <imagem>`       | Remove uma imagem local.                      |
| `docker build -t <nome> .`  | Constrói uma imagem a partir de um Dockerfile. |
| `docker history <imagem>`   | Mostra o histórico de uma imagem.             |

---

## 3. Contêineres

### Criação e Execução

| Comando                                   | Descrição                                      |
|-------------------------------------------|------------------------------------------------|
| `docker run <imagem>`                     | Cria e executa um contêiner a partir de uma imagem. |
| `docker run -d <imagem>`                  | Executa o contêiner em modo desanexado (background). |
| `docker run -it <imagem> /bin/bash`       | Executa o contêiner em modo interativo com shell. |
| `docker run -p 8080:80 <imagem>`          | Mapeia a porta 8080 do host para a porta 80 do contêiner. |
| `docker run --name <nome> <imagem>`       | Define um nome personalizado para o contêiner. |
| `docker start <container>`                | Inicia um contêiner parado.                   |
| `docker stop <container>`                 | Para um contêiner em execução.                |
| `docker restart <container>`              | Reinicia um contêiner.                        |
| `docker rm <container>`                   | Remove um contêiner parado.                   |
| `docker rm -f <container>`                | Força a remoção de um contêiner em execução.  |

---

### Listagem e Inspeção

| Comando                     | Descrição                                      |
|-----------------------------|------------------------------------------------|
| `docker ps`                 | Lista contêineres em execução.                |
| `docker ps -a`              | Lista todos os contêineres (inclusive parados). |
| `docker ps -s`              | Lista contêineres com uso de CPU/memória.     |
| `docker inspect <container>`| Mostra detalhes completos de um contêiner.    |
| `docker logs <container>`   | Exibe os logs de um contêiner.                |
| `docker top <container>`    | Lista os processos em execução no contêiner.  |
| `docker stats`              | Mostra estatísticas de uso de recursos (CPU, memória, etc.). |

---

## 4. Redes

| Comando                     | Descrição                                      |
|-----------------------------|------------------------------------------------|
| `docker network ls`         | Lista todas as redes.                         |
| `docker network create <nome>` | Cria uma nova rede.                        |
| `docker network inspect <nome>` | Mostra detalhes de uma rede.               |
| `docker network rm <nome>`  | Remove uma rede.                              |
| `docker run --network <nome> <imagem>` | Conecta um contêiner a uma rede específica. |

---

## 5. Volumes

| Comando                     | Descrição                                      |
|-----------------------------|------------------------------------------------|
| `docker volume ls`          | Lista todos os volumes.                       |
| `docker volume create <nome>` | Cria um novo volume.                        |
| `docker volume inspect <nome>` | Mostra detalhes de um volume.              |
| `docker volume rm <nome>`   | Remove um volume.                             |
| `docker run -v <volume>:<caminho> <imagem>` | Monta um volume em um contêiner.         |

---

## 6. Docker Compose

### Comandos Básicos

| Comando                     | Descrição                                      |
|-----------------------------|------------------------------------------------|
| `docker-compose up`         | Inicializa os serviços definidos no `docker-compose.yml`. |
| `docker-compose up -d`      | Inicializa os serviços em modo desanexado.    |
| `docker-compose down`       | Para e remove os serviços.                    |
| `docker-compose ps`         | Lista os contêineres dos serviços.            |
| `docker-compose logs`       | Exibe os logs dos serviços.                   |
| `docker-compose build`      | Reconstrói as imagens dos serviços.           |

---

### Estrutura Básica do `docker-compose.yml`

```yaml
version: '3'
services:
  app:
    image: nginx
    ports:
      - "8080:80"
    volumes:
      - ./app:/usr/share/nginx/html
    networks:
      - my-network
networks:
  my-network:
    driver: bridge
```

---

## 7. Dockerfile

### Comandos Comuns

| Comando                     | Descrição                                      |
|-----------------------------|------------------------------------------------|
| `FROM <imagem>`             | Define a imagem base.                         |
| `RUN <comando>`             | Executa um comando durante a construção da imagem. |
| `CMD ["comando"]`           | Define o comando padrão ao iniciar o contêiner. |
| `ENTRYPOINT ["comando"]`    | Define um ponto de entrada fixo para o contêiner. |
| `COPY <origem> <destino>`   | Copia arquivos do host para a imagem.         |
| `ADD <origem> <destino>`    | Adiciona arquivos (suporta URLs e descompactação). |
| `WORKDIR <diretório>`       | Define o diretório de trabalho dentro do contêiner. |
| `EXPOSE <porta>`            | Declara a porta que o contêiner expõe.        |

---

### Exemplo de Dockerfile

```dockerfile
# Usa a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código-fonte
COPY . .

# Expõe a porta 5000
EXPOSE 5000

# Define o comando padrão
CMD ["python", "app.py"]
```

---

## 8. Dicas e Melhores Práticas

- **Use tags explícitas**: Evite usar `latest` ao baixar imagens. Use tags específicas, como `nginx:1.23`.
- **Limpeza regular**: Remova contêineres, imagens e volumes não utilizados com:
  ```bash
  docker system prune -a
  ```
- **Evite root**: Execute contêineres como usuário não root sempre que possível.
- **Minimize camadas**: Combine múltiplos comandos `RUN` em um único comando para reduzir o tamanho da imagem.

---

## 9. Ferramentas Úteis

- [Docker Hub](https://hub.docker.com/) - Repositório oficial de imagens Docker.
- [Play with Docker](https://labs.play-with-docker.com/) - Ambiente online para testar Docker.
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) - Interface gráfica para gerenciar Docker.

---

## Observações Finais
Este cheatsheet foi projetado para ser uma referência rápida e prática. Para obter mais detalhes sobre qualquer comando ou conceito específico, consulte a [documentação oficial do Docker](https://docs.docker.com/).

---
