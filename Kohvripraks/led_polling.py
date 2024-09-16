import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

leds = [11, 13, 22, 24, 26, 36]
# 11 - JK punane
# 13 - JK roheline
# 22 - Auto punane
# 24 - Auto kollane
# 26 - Auto roheline
# 36 - Valge
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Nupp
#Nupp muidu HIGH, vajutades on LOW
button_pressed_led = 11
try:
    while True:
        button_state = GPIO.input(37)
        GPIO.output(22, GPIO.HIGH) #Punane sisse
        GPIO.output(button_pressed_led, GPIO.HIGH) #JK sisse
        sleep(4)
        if GPIO.input(37) == GPIO.LOW: 
            button_state = GPIO.LOW
            GPIO.output(36, GPIO.HIGH) #Valge sisse
        sleep(1)
        GPIO.output(36, GPIO.LOW) #Valge välja
        GPIO.output(22, GPIO.LOW) #Punane välja
        GPIO.output(button_pressed_led, GPIO.LOW) #JK välja
        GPIO.output(24, GPIO.HIGH) #Kollane sisse
        GPIO.output(11, GPIO.HIGH) #JK punane sisse
        if GPIO.input(37) == GPIO.LOW: 
            button_state = GPIO.LOW
            GPIO.output(36, GPIO.HIGH) #Valge sisse
        sleep(1)
        GPIO.output(36, GPIO.LOW) #Valge välja
        GPIO.output(24, GPIO.LOW) #Kollane välja
        GPIO.output(26, GPIO.HIGH) #Roheline sisse
        sleep(4)
        if GPIO.input(37) == GPIO.LOW: 
            button_state = GPIO.LOW
            GPIO.output(36, GPIO.HIGH) #Valge sisse
        sleep(1)
        GPIO.output(36, GPIO.LOW) #Valge välja
        GPIO.output(26, GPIO.LOW) #Roheline välja

        #Kollane vilkuma
        for _ in range(3):
            GPIO.output(24, GPIO.HIGH) #Kollane sisse
            if GPIO.input(37) == GPIO.LOW: 
                button_state = GPIO.LOW
                GPIO.output(36, GPIO.HIGH) #Valge sisse
            sleep(2/6)
            GPIO.output(24, GPIO.LOW) #Kollane välja
            if GPIO.input(37) == GPIO.LOW: 
                button_state = GPIO.LOW
                GPIO.output(36, GPIO.HIGH) #Valge sisse
            sleep(2/6)
            GPIO.output(36, GPIO.LOW) #Valge välja
        
        GPIO.output(11, GPIO.LOW) #JK punane välja
        sleep(0.01)
        if GPIO.input(37) == GPIO.LOW: 
            button_state = GPIO.LOW
            GPIO.output(36, GPIO.HIGH) #Valge sisse

        #Nupu kontrollija
        if button_state == GPIO.LOW:
            print("Button was pressed!")
            button_pressed_led = 13
        else:
            print("Button was not pressed!")
            button_pressed_led = 11
except KeyboardInterrupt:
    print("\nKeyboard interrupt")
finally:
    GPIO.output(leds, False)
    GPIO.cleanup(leds)