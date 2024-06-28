from machine import WDT, Pin
import time

led = Pin(16, Pin.OUT)
PIR = Pin(15, Pin.IN)
PIRflag = False

def handFunc(pin):
    global PIRflag
    PIRflag = True

wdt = WDT(timeout=2000) # enable the watchdog timer with timeout of 2000ms
PIR.irq(trigger=Pin.IRQ_RISING, handler=handFunc) # call handler func when rising edge on pin 15 is detected
#PIR sensor needs 5sec to initialise
for i in range(5):
    time.sleep(1)
    wdt.feed()

while(True):
    PIRflag = False
    state = machine.disable_irq()
    PIRtempVal = PIRflag
    machine.enable_irq(state)
    if(PIRtempVal == True):
        led.value(0) # logic of the led board is invertered so logic level means leds turned off etc.
        for i in range(60):
            time.sleep(1)
            wdt.feed()
    state = machine.disable_irq()
    PIRflag = False
    machine.enable_irq(state)
    led.value(1)
    wdt.feed()
