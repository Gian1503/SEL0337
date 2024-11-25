# Import das bibliotecas
from gpiozero import LED
from time import sleep

# Associação do LED ao pino GPIO 18 do Raspberry Pi
PinLED = LED(18)

# Loop infinito para alternar o estado do LED
while True:  
    PinLED.on()  # Liga o LED 
    sleep(1)     # Aguarda 1 segundo 
    PinLED.off() # Desliga o LED 
    sleep(1)     # Aguarda 1 segundo
