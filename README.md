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

import RPi.GPIO as GPIO
import time

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN = 18  # Pino GPIO conectado ao LED
GPIO.setup(PIN, GPIO.OUT)

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
    Este código controla o piscar de um LED conectado ao pino GPIO 18 da Raspberry Pi. Ele utiliza a biblioteca RPi.GPIO, que permite interagir com os pinos GPIO de forma simples. A biblioteca time é usada para criar os intervalos de tempo entre os estados do LED.

Primeiro, o código define o modo de numeração dos pinos como BCM, que corresponde à numeração do processador, e desativa avisos com GPIO.setwarnings(False). Em seguida, configura o pino GPIO 18 como saída, pois ele será usado para ligar e desligar o LED.

No loop principal, o LED alterna entre ligado (HIGH) e desligado (LOW) com intervalos de 0,2 segundos, criando o efeito de piscar continuamente. Se o script for interrompido com Ctrl+C, o código limpa as configurações dos pinos GPIO para evitar problemas em futuras execuções.
