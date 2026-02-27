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


# Raspberry Pi Pico no Arch Linux

## 1. Toolchain de Compilação Cruzada

Instalação dos utilitários do sistema operacional e compiladores ARM nativos do Arch Linux.

```bash
sudo pacman -Syu --needed cmake arm-none-eabi-gcc arm-none-eabi-newlib arm-none-eabi-gdb git python base-devel usbutils
```

## 2. Provisionamento do SDK (Framework Base)

Clonagem das bibliotecas de hardware no espaço do usuário e configuração do caminho no shell.

```bash
mkdir -p ~/projetos/pico
cd ~/projetos/pico
git clone https://github.com/raspberrypi/pico-sdk.git
cd pico-sdk
git submodule update --init

echo "export pico_sdk_path=$home/projetos/pico/pico-sdk" >> ~/.bashrc
source ~/.bashrc

# ou
# echo "export pico_sdk_path=$home/projetos/pico/pico-sdk" >> ~/.zshrc
# source ~/.zshrc

```

## 3. Integração do Repositório de Exemplos

Download da biblioteca oficial de implementações de referência.

```bash
cd ~/projetos/pico
git clone https://github.com/raspberrypi/pico-examples.git
```

## 4. Estruturação da Árvore de Build (Root Context)

A execução do cmake deve ocorrer obrigatoriamente na raiz do repositório pico-examples. Isso garante que as macros do SDK (pico_add_extra_outputs) sejam lidas corretamente pelo compilador antes de atingir os subprojetos.

```bash
cd ~/projetos/pico/pico-examples
mkdir -p build && cd build
cmake ..
```

## 5. Compilação Direcionada (Módulo Blink)

Com o mapeamento de dependências estabelecido na raiz, compila-se exclusivamente o binário alvo utilizando múltiplos núcleos do processador para otimização de tempo.

```bash
cd blink
make -j$(nproc)
```

## 6. Montagem e Cópia (Deploy no Hardware)

### Conectando o Raspberry Pi Pico

O dispositivo aparecerá como uma unidade de armazenamento removível (geralmente montada automaticamente em distribuições modernas).

### Verificação e Montagem (se necessário)

Caso o Pico não monte automaticamente, verifique se o sistema o reconheceu:

```bash
lsblk | grep sda
```

Se aparecer como /dev/sda1 (ou similar), monte manualmente:

```bash
# Criar ponto de montagem (se não existir)
sudo mkdir -p /mnt/pico

# Montar o dispositivo
sudo mount /dev/sda1 /mnt/pico
```

### Transferência do Binário

```bash
# Verificar se o arquivo .uf2 foi gerado corretamente
ls -la ~/projetos/pico/pico-examples/build/blink/blink.uf2

# Copiar o arquivo para o Pico
sudo cp ~/projetos/pico/pico-examples/build/blink/blink.uf2 /mnt/pico/

# Garantir que a gravação foi concluída
sudo sync
```


## Validação do Deploy

O provisionamento está concluído. O microcontrolador executará o *reboot* automaticamente e iniciará a leitura do binário na memória Flash. A alternância contínua de estado lógico do LED *onboard* (GPIO 25) confirma a integridade ponta a ponta da *toolchain* do Arch Linux e a operação do hardware.

{{< figure src="/gif/blink_pico.gif" alt="Blink Pico" width="300px" >}}

## Finalização
Após a cópia, o Pico reiniciará automaticamente e executará o programa. Se desejar, você pode desmontar manualmente a unidade:

```bash
sudo umount /mnt/pico
