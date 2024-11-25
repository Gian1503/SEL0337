import RPi.GPIO as GPIO

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Desliga o LED e limpa os pinos
GPIO.output(18, GPIO.LOW)
GPIO.cleanup()