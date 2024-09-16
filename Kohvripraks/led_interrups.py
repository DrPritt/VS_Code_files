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
button_pressed = False
pedestrian_request = False

def nuppu_vajutus(nupu_pin):
    global button_pressed
    button_pressed = True
    while True:
        if GPIO.input(nupu_pin) == GPIO.LOW:
            GPIO.output(36, GPIO.HIGH)
        else: 
            GPIO.output(36, GPIO.LOW)
            break
        sleep(.01)

GPIO.add_event_detect(37, GPIO.FALLING, callback=nuppu_vajutus, bouncetime=300)

try:
    while True:
        if button_pressed:
            print("Button has been pressed!")
            pedestrian_request = True
            button_pressed = False
        else:
            print("Button was not pressed!")
            pedestrian_request = False
        GPIO.output(22, GPIO.HIGH) #Punane sisse
        if pedestrian_request:
            button_pressed_led = 13
        else: 
            button_pressed_led = 11
        GPIO.output(button_pressed_led, GPIO.HIGH) #JK sisse
        sleep(5)
        GPIO.output(22, GPIO.LOW) #Punane välja
        GPIO.output(button_pressed_led, GPIO.LOW) #JK välja
        GPIO.output(24, GPIO.HIGH) #Kollane sisse
        GPIO.output(11, GPIO.HIGH) #JK punane sisse
        sleep(1)
        GPIO.output(24, GPIO.LOW) #Kollane välja
        GPIO.output(26, GPIO.HIGH) #Roheline sisse
        sleep(5)
        GPIO.output(26, GPIO.LOW) #Roheline välja

        #Kollane vilkuma
        for _ in range(3):
            GPIO.output(24, GPIO.HIGH) #Kollane sisse
            sleep(2/6)
            GPIO.output(24, GPIO.LOW) #Kollane välja
            sleep(2/6)

        GPIO.output(11, GPIO.LOW) #JK punane välja
        sleep(0.01)
except KeyboardInterrupt:
    print("\nKeyboard interrupt")
finally:
    GPIO.output(leds, False)
    GPIO.cleanup(leds)