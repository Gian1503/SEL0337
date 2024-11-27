# SEL0337
PRATICA 5
# Projeto Blink LED com SystemD

Este repositório documenta a prática de configuração de um serviço personalizado utilizando `systemd` em uma Raspberry Pi. O objetivo do projeto é demonstrar como configurar um script para ser executado automaticamente no boot, gerenciando o piscar de um LED conectado a um GPIO da placa.

## Funcionamento do Projeto

O projeto consiste em:
1. **2 Scripts Python (`blink.py`)**: Responsáveis por controlar o GPIO para alternar o estado do LED e parar o serviço uma vez que desejado.
2. **Arquivo de Serviço (`blink2524.service`)**: Arquivo que configura o `systemd` para gerenciar o script, permitindo sua inicialização automática no boot.
3. **Gerenciamento com Git/GitHub**: Controle de versão dos arquivos e documentação do projeto, com histórico completo dos commits.

### Etapas Implementadas
1. **Criação dos Scripts (`blink.py` e `stop_blink.py`)**:
   - O primeiro script exporta e configura o GPIO 18 como saída, alternando o estado do LED em um loop infinito.
   - O segudno script é responsável por interromper o serviço, apagando o LED indefinidamente.

2. **Configuração do Serviço (`blink2524.service`)**:
   - Define o script como o processo a ser executado no boot.
   - Permite controle manual utilizando `systemctl` (start, stop, enable, disable).

3. **Documentação e Controle de Versão**:
   - Todos os arquivos e alterações estão registrados neste repositório Git.
   - O histórico de commits pode ser consultado no arquivo `historico_git.txt`.

## Fotografia da Montagem
- A montagem prática do circuito pode ser vista na imagem abaixo:

<div align="center">
<img src="https://github.com/user-attachments/assets/cfb7eff5-4f56-4d57-8b45-3468f3264a75" width="500px" />
</div>

# Projeto Blink LED com Raspberry Pi

Este projeto demonstra como criar um programa em Python para fazer um LED piscar usando os pinos GPIO da Raspberry Pi.

## Códigos Python
# Projeto de Controle de LED Blink

Esta seção contém um projeto simples de controle de LED, com dois comandos para acender e apagar o LED com um intervalo de 1 segundo. O primeiro código utiliza a biblioteca `gpiozero` para controle diretamente no Raspberry Pi.

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
```
## Código 2: Interrompição do serviço de acendimento do LED (Python)
o segundo código é uma configuração de serviço no systemd para gerenciar o blink do LED.
