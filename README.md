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


# Projeto de Controle de LED - códigos python

Esta seção contém um projeto simples de controle de LED, com dois comandos para acender e apagar o LED com um intervalo de 1 segundo. O primeiro código utiliza a biblioteca `gpiozero` para controle diretamente no Raspberry Pi.

## Código 1: blink.py

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
## Código 2: stop_blink.py
Esse código utiliza a biblioteca RPi.GPIO para desligar o LED ligado ao pino GPIO 18 e libera os recursos associados aos pinos GPIO utilizados no programa, retornando-os ao estado inicial para evitar conflitos em futuros usos.

```python
import RPi.GPIO as GPIO

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Desliga o LED e limpa os pinos
GPIO.output(18, GPIO.LOW)
GPIO.cleanup()
```
## Código 3: blink2524.service
O terceiro código é um unit file, que é responsável pela configuração do serviço no systemd para gerenciar os códigos blink.py e stop_blink.py, colocando o
serviço que criamos à disposição do systemd.

```
[Unit]
Description=Blink LED 
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /home/sel/blink.py
ExecStop=/usr/bin/python3 /home/sel/stop_blink.py
User=sel

[Install]
WantedBy=multi-user.target
```

