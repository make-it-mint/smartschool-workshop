'''
Es gibt noch eine Möglichkeit die Funktion für Nutzende einfacher zu gestalten. Den Argumenten können "Defaultwerte" zugewiesen werden.
Diese Werte bekommen die Argumente automatisch, wenn ihnen beim Aufrufen keine Werte übergeben werden.
Setze für alle Argumente jeweils einen "Defaultwert".
Die Lösung findest du in ch_12. 
'''

from machine import Pin
import time, math


def led_blinken(num_loops, led_pin, pause):
    led = Pin(led_pin, Pin.OUT)
    for i in range(1,num_loops+1):
        led.toggle()
        time.sleep(pause)
        print(f"LED hat {math.ceil(i/2)}x geblinkt, Schaltperiode = {pause} Sekunden")
        pause = 0.9 * pause
    return i

print(led_blinken(num_loops=100, led_pin="LED",pause=0.5))

