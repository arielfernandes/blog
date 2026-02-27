---
title: "Desenvolvimento com Raspberry Pi Pico no Arch Linux"
description: "Guia técnico para setup da toolchain ARM, compilação via CMake e deploy de firmware no RP2040."
slug: "pico-pi-arch-linux"
author: "Ariel Fernandes"
date: 2026-02-26
draft: false
categories: ["Sistemas Embarcados", "Engenharia de Software"]
tags: ["raspberry-pi-pico", "rp2040", "arch-linux", "cpp", "cmake"]
type: "posts"
---

Protocolo Oficial: Deploy do Exemplo Blink (Pico SDK) no Arch Linux
1. Toolchain de Compilação Cruzada

Instalação dos utilitários do sistema operacional e compiladores ARM nativos do Arch Linux.
Bash

sudo pacman -Syu --needed cmake arm-none-eabi-gcc arm-none-eabi-newlib arm-none-eabi-gdb git python base-devel usbutils

2. Provisionamento do SDK (Framework Base)

Clonagem das bibliotecas de hardware no espaço do usuário e injeção do caminho no shell.
Bash

mkdir -p ~/projetos/pico
cd ~/projetos/pico
git clone https://github.com/raspberrypi/pico-sdk.git
cd pico-sdk
git submodule update --init

echo "export PICO_SDK_PATH=$HOME/projetos/pico/pico-sdk" >> ~/.bashrc
source ~/.bashrc

3. Integração do Repositório de Exemplos

Download da biblioteca oficial de implementações de referência.
Bash

cd ~/projetos/pico
git clone https://github.com/raspberrypi/pico-examples.git

4. Estruturação da Árvore de Build (Root Context)

A execução do cmake deve ocorrer obrigatoriamente na raiz do repositório pico-examples. Isso garante que as macros do SDK (pico_add_extra_outputs) sejam lidas corretamente pelo compilador antes de atingir os subprojetos.
Bash

cd ~/projetos/pico/pico-examples
mkdir -p build && cd build
cmake ..

5. Compilação Direcionada (Módulo Blink)

Com o mapeamento de dependências estabelecido na raiz, compila-se exclusivamente o binário alvo utilizando múltiplos núcleos do processador para otimização de tempo.
Bash

cd blink
make -j$(nproc)

6. Flash (Deploy no Hardware)

Transferência do arquivo de firmware .uf2 para a memória da placa.

A. Ativação do Bootrom (Hardware)

    Desconecte o cabo USB do Pico.

    Mantenha pressionado o botão BOOTSEL.

    Conecte o cabo USB.

    Solte o botão após 2 segundos.

    Verifique o identificador do bloco montado (ex: sda1) executando lsblk.

B. Montagem e Cópia (Software)
Bash

# Criação do ponto de montagem
sudo mkdir -p /mnt/pico

# Montagem da partição FAT16
sudo mount /dev/sda1 /mnt/pico

# Transferência do binário
sudo cp blink.uf2 /mnt/pico/

# Sincronização forçada (Garante a gravação antes do auto-reboot)
sudo sync

**Validação do Deploy:**
O provisionamento está concluído. O microcontrolador executará o *reboot* automaticamente e iniciará a leitura do binário na memória Flash. A alternância contínua de estado lógico do LED *onboard* (GPIO 25) confirma a integridade ponta a ponta da *toolchain* do Arch Linux e a operação do hardware.
