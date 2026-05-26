'''
In dieser Challenge soll der Funktion "led_blinken" ein Argument hinzugefügt werden, dass festlegt, wie oft die for-Schleife durchlaufen wird.
Das Argument soll den Namen "num_loops" haben und in der Funktion die Anzahl der for-Schleifen Durchläufe festlegen
Die Lösung findest du in ch_10. 
'''

from machine import Pin
import time, math


def led_blinken():
    pause = 0.5
    led = Pin("LED", Pin.OUT)
    for i in range(1,201):
        led.toggle()
        time.sleep(pause)
        print(f"LED hat {math.ceil(i/2)}x geblinkt, Schaltperiode = {pause} Sekunden")
        pause = 0.9 * pause
    return i

print(led_blinken())
