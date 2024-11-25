# SEL0337
PRATICA 5
# Projeto Blink LED com SystemD

Este repositório documenta a prática de configuração de um serviço personalizado utilizando `systemd` em uma Raspberry Pi. O objetivo do projeto é demonstrar como configurar um script para ser executado automaticamente no boot, gerenciando o piscar de um LED conectado a um GPIO da placa.

## Funcionamento do Projeto

O projeto consiste em:
1. **Script Python (`blink.py`)**: Controla o GPIO para alternar o estado do LED.
2. **Arquivo de Serviço (`blink2524.service`)**: Configura o `systemd` para gerenciar o script, permitindo sua inicialização automática no boot.
3. **Gerenciamento com Git/GitHub**: Controle de versão dos arquivos e documentação do projeto, com histórico completo dos commits.

### Etapas Implementadas
1. **Criação do Script (`blink.py`)**:
   - Exporta e configura o GPIO 18 como saída.
   - Alterna o estado do LED em um loop infinito.

2. **Configuração do Serviço (`blink2524.service`)**:
   - Define o script como o processo a ser executado no boot.
   - Permite controle manual utilizando `systemctl` (start, stop, enable, disable).

3. **Documentação e Controle de Versão**:
   - Todos os arquivos e alterações estão registrados neste repositório Git.
   - O histórico de commits pode ser consultado no arquivo `historico_git.txt`.

## Fotografias da Montagem
- A montagem prática do circuito pode ser vista na imagem abaixo:
  ![Montagem do Circuito](link_para_fotografia)



## Comandos Principais

# Projeto Blink LED com Raspberry Pi

Este projeto demonstra como criar um programa em Python para fazer um LED piscar usando os pinos GPIO da Raspberry Pi.

## Código Python
# Projeto de Controle de LED Blink

Este repositório contém um projeto simples de controle de LED, com dois métodos para acender e apagar o LED com um intervalo de 1 segundo. O primeiro código utiliza a biblioteca `gpiozero` para controle diretamente no Raspberry Pi, e o segundo código é uma configuração de serviço no systemd para gerenciar o blink do LED.

## Código 1: Blink com GPIOZero (Python)

Este código utiliza a biblioteca `gpiozero` para controlar um LED no Raspberry Pi. O LED acende e apaga a cada 1 segundo.

```python
from gpiozero import LED
from time import sleep

PinLED = LED(18)

while True:
    PinLED.on()
    sleep(1)
    PinLED.off()
    sleep(1)

