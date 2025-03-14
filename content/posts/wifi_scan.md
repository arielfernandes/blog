---
title: "Mapeando Redes Wi-Fi com ESP32 e Display OLED"
author: Ariel Fernandes
date: 2025-03-14
draft: false
tags: ["esp32"]
type: "posts"
---

Este tutorial detalha como usar um **ESP32** para mapear redes Wi-Fi disponíveis e exibir os resultados em um display OLED. O código utiliza a biblioteca **WiFi.h** para escanear as redes Wi-Fi e a biblioteca **SSD1306.h** para controlar o display OLED.

---

## **Componentes Necessários**

1. **ESP32**: O modelo utilizado neste exemplo é o **ESP32 DevKit V1** (com chip ESP-WROOM-32). Este é um dos modelos mais comuns e amplamente utilizados.
2. **Display OLED SSD1306**: Com resolução de 128x64 pixels, conectado via interface I2C.
3. **Cabos de Conexão**: Para conectar o ESP32 ao display OLED.
4. **Computador**: Para programar o ESP32 usando o Arduino IDE.

---

## **Conexões Físicas**

A tela OLED SSD1306 geralmente usa a interface **I2C**, que requer apenas dois pinos de dados (`SDA` e `SCL`) além da alimentação (`VCC` e `GND`). Abaixo estão as conexões típicas:

| Pino OLED | Pino ESP32 |
|-----------|------------|
| VCC       | 3.3V       |
| GND       | GND        |
| SDA       | GPIO21     |
| SCL       | GPIO22     |

> **Nota:** Os pinos GPIO21 (SDA) e GPIO22 (SCL) são os pinos padrão do ESP32 para comunicação I2C.

---

## **Bibliotecas Necessárias**

Para este projeto, você precisará das seguintes bibliotecas:

1. **WiFi.h**: Biblioteca padrão do ESP32 para gerenciar a funcionalidade Wi-Fi.
2. **SSD1306.h**: Biblioteca para controlar o display OLED baseado no controlador SSD1306.

#### **Instalação das Bibliotecas**
1. Abra o Arduino IDE.
2. Vá para **Ferramentas > Gerenciar Bibliotecas**.
3. Procure e instale as seguintes bibliotecas:
   - `SSD1306.h` (para controle do display OLED).
   - A biblioteca `WiFi.h` já está incluída no ambiente de desenvolvimento do ESP32.

---

## **Código Completo**

```cpp
#include <Wire.h>
#include "SSD1306.h" // Certifique-se de que esta é a biblioteca correta
#include <WiFi.h>    // Biblioteca WiFi do ESP32

// Inicialize o display OLED
SSD1306 display(0x3C, 5, 4);

void setup() {
  // Inicialize a comunicação serial para debug
  Serial.begin(115200);

  // Inicialize o display OLED
  display.init();
  display.clear();
  display.flipScreenVertically(); // Opcional: vire a tela verticalmente se necessário
  display.setFont(ArialMT_Plain_10); // Defina a fonte inicial

  // Exiba uma mensagem inicial no display
  display.drawString(0, 0, "Escaneando Wi-Fi...");
  display.display();

  // Desconecte do Wi-Fi atual, se conectado
  WiFi.disconnect();
  delay(100);

  // Inicie o escaneamento de redes Wi-Fi
  int numberOfNetworks = WiFi.scanNetworks();
  display.clear();

  if (numberOfNetworks == 0) {
    display.drawString(0, 0, "Nenhuma rede encontrada");
  } else {
    display.drawString(0, 0, "Redes Wi-Fi:");
    for (int i = 0; i < numberOfNetworks; i++) {
      String ssid = WiFi.SSID(i); // Obtenha o SSID da rede
      int32_t rssi = WiFi.RSSI(i); // Obtenha a força do sinal (RSSI)

      // Exiba o SSID e a força do sinal no display
      String networkInfo = String(i + 1) + ": " + ssid + " (" + String(rssi) + " dBm)";
      display.drawString(0, 10 + (i * 10), networkInfo);
    }
  }

  // Atualize o display com os resultados
  display.display();
}

void loop() {
  // Nada a fazer no loop
}
```

---

## **Explicação Detalhada do Código**

### **1. Inicialização do Display OLED**

```cpp
SSD1306 display(0x3C, 5, 4);
```

- O objeto `display` é criado com o endereço I2C padrão (`0x3C`) e os pinos `SDA` e `SCL` configurados como GPIO5 e GPIO4 (ajuste conforme necessário para o seu hardware).

```cpp
display.init();
display.clear();
```

- O método `init()` inicializa o display OLED.
- O método `clear()` limpa o buffer do display.

---

### **2. Escaneamento de Redes Wi-Fi**

```cpp
WiFi.disconnect();
delay(100);
int numberOfNetworks = WiFi.scanNetworks();
```

- `WiFi.disconnect()` desconecta o ESP32 de qualquer rede Wi-Fi ativa.
- `WiFi.scanNetworks()` escaneia as redes Wi-Fi disponíveis e retorna o número de redes encontradas.

---

### **3. Exibição dos Resultados no Display**

```cpp
if (numberOfNetworks == 0) {
  display.drawString(0, 0, "Nenhuma rede encontrada");
} else {
  display.drawString(0, 0, "Redes Wi-Fi:");
  for (int i = 0; i < numberOfNetworks; i++) {
    String ssid = WiFi.SSID(i); // Obtenha o SSID da rede
    int32_t rssi = WiFi.RSSI(i); // Obtenha a força do sinal (RSSI)

    String networkInfo = String(i + 1) + ": " + ssid + " (" + String(rssi) + " dBm)";
    display.drawString(0, 10 + (i * 10), networkInfo);
  }
}
```

- Se nenhuma rede for encontrada, o display exibirá "Nenhuma rede encontrada".
- Caso contrário, o código exibirá uma lista das redes Wi-Fi encontradas, incluindo o SSID e a força do sinal (em dBm).

---

### **4. Atualização do Display**

```cpp
display.display();
```

- O método `display()` envia o conteúdo do buffer para o display OLED.

---

## **Resultados Esperados**

1. Quando o ESP32 é iniciado:
   - O display OLED exibirá a mensagem inicial: `"Escaneando Wi-Fi..."`.
   - Após o escaneamento, o display mostrará uma lista das redes Wi-Fi disponíveis, incluindo o SSID e a força do sinal (RSSI).

2. Exemplo de saída no display:
   ```
   Redes Wi-Fi:
   1: Rede1 (-50 dBm)
   2: Rede2 (-60 dBm)
   3: Rede3 (-70 dBm)
   ```

---

## **Solução de Problemas**

### **1. Display Não Funciona**
- Verifique o endereço I2C do display usando um scanner I2C.
  ```cpp
  #include <Wire.h>

  void setup() {
    Serial.begin(115200);
    Wire.begin();
    Serial.println("Scanning I2C devices...");
    byte error, address;
    int nDevices = 0;
    for (address = 1; address < 127; address++) {
      Wire.beginTransmission(address);
      error = Wire.endTransmission();
      if (error == 0) {
        Serial.print("I2C device found at address 0x");
        Serial.println(address, HEX);
        nDevices++;
      }
    }
    if (nDevices == 0) {
      Serial.println("No I2C devices found");
    }
  }

  void loop() {}
  ```

### **2. Nenhuma Rede Encontrada**
- Certifique-se de que o ESP32 está em um local com redes Wi-Fi disponíveis.
- Verifique se o módulo Wi-Fi do ESP32 está funcionando corretamente.

---

## **Conclusão**

Este tutorial demonstrou como usar um ESP32 para mapear redes Wi-Fi e exibir os resultados em um display OLED. O código é simples e pode ser expandido para incluir funcionalidades adicionais, como filtragem de redes ou exibição de informações detalhadas sobre cada rede.

