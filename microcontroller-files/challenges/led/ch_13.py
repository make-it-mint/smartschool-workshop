'''
Außer der Umbenennung des Arguments musst du noch die Anzahl der Schleifendurchläufe verdoppeln,
da jedes Blinken zwei Durchläufe der Schleife erfordert.
Super, du hast jetzt eine flexibel einsetzbare Funktionen zum Blinken einer LED.
Passe den Inhalt der Funktion an, solltest du ein anderes Verhalten benötigen.
'''

from machine import Pin
import time, math


def led_blinken(num_blinken=100, led_pin="LED", pause=0.5):
    led = Pin(led_pin, Pin.OUT)
    for i in range(1,num_blinken*2+1):
        led.toggle()
        time.sleep(pause)
        print(f"LED hat {math.ceil(i/2)}x geblinkt, Schaltperiode = {pause} Sekunden")
        pause = 0.9 * pause
    return i

#Aufruf nur mit Defaultwerten
print(led_blinken())

#Aufruf mit einem geänderten Wert für "num_blinken" und "pause"
print(led_blinken(num_blinken=300, pause=1))



