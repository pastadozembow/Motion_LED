from machine import WDT, Pin, Timer, Counter, Time
wdt = WDT(timeout=2000) # enable the watchdog timer with timeout of 100ms
led = Pin(16, Pin.OUT)
PIR = Pin(15, Pin.IN)
bool PIRon = false
def handler(timer):
    if(PIR.value() == 1):
        PIRon = true
    else:
        PIRon = false
while(true):
    if(PIRon == true):
        led.value(1)
        for i in range(60):
            time.sleep(1)
            wdt.feed()
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=handler) # enable a periodic timer to check when PIR triggers
wdt.feed()