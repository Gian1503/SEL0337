# SEL0337
PRATICA 5
# Projeto Blink LED com SystemD

Este repositório documenta a prática de configuração de um serviço personalizado utilizando `systemd` em uma Raspberry Pi. O objetivo do projeto é demonstrar como configurar um script para ser executado automaticamente no boot, gerenciando o piscar de um LED conectado a um GPIO da placa.

## Funcionamento do Projeto

O projeto consiste em:
1. **Script Bash (`blink.sh`)**: Controla o GPIO para alternar o estado do LED.
2. **Arquivo de Serviço (`blink.service`)**: Configura o `systemd` para gerenciar o script, permitindo sua inicialização automática no boot.
3. **Gerenciamento com Git/GitHub**: Controle de versão dos arquivos e documentação do projeto, com histórico completo dos commits.

### Etapas Implementadas
1. **Criação do Script (`blink.sh`)**:
   - Exporta e configura o GPIO 18 como saída.
   - Alterna o estado do LED em um loop infinito.

2. **Configuração do Serviço (`blink.service`)**:
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

O código abaixo faz o LED piscar continuamente com intervalos de 0,2 segundos.

```python
import RPi.GPIO as GPIO
import time

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)  # Define o modo de numeração dos pinos como BCM
GPIO.setwarnings(False)  # Desativa mensagens de aviso sobre o uso dos GPIOs

PIN = 18  # Pino GPIO conectado ao LED
GPIO.setup(PIN, GPIO.OUT)  # Configura o pino como saída

try:
    while True:
        GPIO.output(PIN, GPIO.HIGH)  # Liga o LED
        time.sleep(0.2)             # Aguarda 0.2 segundos
        GPIO.output(PIN, GPIO.LOW)  # Desliga o LED
        time.sleep(0.2)             # Aguarda 0.2 segundos
except KeyboardInterrupt:
    GPIO.cleanup()  # Limpa as configurações do GPIO ao encerrar o script

