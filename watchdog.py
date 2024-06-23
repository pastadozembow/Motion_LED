from machine import WDT, Pin, Timer, Counter,
import time, mutex

led = Pin(16, Pin.OUT)
PIR = Pin(15, Pin.IN)
mutex = mutex.Mutex()
bool PIRval = false

def handler(timer):
    if mutex.test():
        data_ready = True
        global PIRval = true
        mutex.release()

wdt = WDT(timeout=2000) # enable the watchdog timer with timeout of 2000ms
PIR.irq(trigger=Pin.IRQ_RISING, handler=handler) # eable irq interrupt when rising edge on pin 15 is detected

while(true):
    if(PIRval == true):
        led.value(1)
        for i in range(60):
            time.sleep(1)
            wdt.feed()
    with mutex:
        PIRval = false
    led.value(0)
    wdt.feed()
            
