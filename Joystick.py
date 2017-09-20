import RPi.GPIO as GPIO
from time import sleep

##### input pins ####
upSwitchPin = 13
downSwitchPin = 5
leftSwitchPin = 6
rightSwitchPin = 19

#### output pins ####
light1 = 21
light2 = 20
light3 = 16
light4 = 12
light5 = 25
fan = 18

#### initialize setup ####
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# initial set-up for input pins
inputList = [upSwitchPin, downSwitchPin, leftSwitchPin, rightSwitchPin]
wordList = ["u", "d", "l", "r"]
for i in range(len(inputList)):
    GPIO.setup(inputList[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

# initial set-up for output LED pins and the fan
ledList = [light1, light2, light3, light4, light5]
for i in range(len(ledList)):
    GPIO.setup(ledList[i], GPIO.OUT)
    GPIO.output(ledList[i], 0)

GPIO.setup(fan, GPIO.OUT)
GPIO.output(fan, 0)

# function to turn on all LEDs
def onAll():
    for i in range(len(ledList)):
        GPIO.output(ledList[i], 1)
    sleep(0.5)

# function to turn off all LEDs
def offAll():
    for i in range(len(ledList)):
        GPIO.output(ledList[i], 0)
    sleep(0.5)

# function to flash all the lights three times
def flashAll():
    onAll()
    offAll()
    onAll()
    offAll()
    onAll()
    offAll()
    onAll()
    offAll()
    onAll()
    offAll()
    onAll()
    offAll()

#### MAIN ####
answer = ""
key = "lllll"

try:
    while(True):
        for i in range(len(inputList)):
            if GPIO.input(inputList[i]) == 0:
                sleep(0.5)
                print(wordList[i] + " is pressed")
                answer += wordList[i]
                print("the current answer is:" + answer)
                print(str(len(answer)) + " LEDs should be on")
                
                for j in range(len(answer)):
                    GPIO.output(ledList[j], 1)
                
                if len(answer) < 5:
                    print("continue")
                elif len(answer) == 5:
                    print("5 inputs!")
                    sleep(1)
                    if answer == key:
                          print("correct!")
                          GPIO.output(fan, 1)
                          flashAll()
                          GPIO.output(fan, 0)
                    else:
                          print("wrong!")
                    for j in range(len(answer)):
                        GPIO.output(ledList[j], 0)
                    answer = ""
                else:
                    for j in range(len(answer)):
                        print("max input!")
                        GPIO.output(ledList[j], 0)
                        answer = ""
                
    
        
        
except KeyboardInterrupt:
    GPIO.cleanup()
