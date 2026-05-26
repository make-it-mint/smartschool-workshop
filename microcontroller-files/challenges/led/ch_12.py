'''
Super, jetzt ist die Funktion flexibel einsetzbar. Du könntest das Argument für "num_loops" noch anpassen, damit es angeibt, wie oft die LED blinkt.
Was musst du dafür machen? Benne das Argument "num_loops" in "num_blinken" um und passe deine Funktion an.
Die Lösung findest du in ch_13.
'''

from machine import Pin
import time, math


def led_blinken(num_loops=100, led_pin="LED", pause=0.5):
    led = Pin(led_pin, Pin.OUT)
    for i in range(1,num_loops+1):
        led.toggle()
        time.sleep(pause)
        print(f"LED hat {math.ceil(i/2)}x geblinkt, Schaltperiode = {pause} Sekunden")
        pause = 0.9 * pause
    return i

#Aufruf nur mit Defaultwerten
print(led_blinken())

#Aufruf mit einem geänderten Wert für "pause"
print(led_blinken(pause=1))


