'''
Die LED wird in jedem Durchlauf entweder an oder aus geschalten. Der Vorteil der "toggle" Methode ist, dass sie den aktuellen Zustand
des Pins erkennt und ihn ändert. Wird beispielsweise die "off" Methode verwendet und der Pin ist im "off" Zustand, ändert sich nichts.

Ändere deinen Code jetzt so,dass dein Programm innerhalb einer Funktion "led_blinken" enthalten ist.
Die Funktion soll zurückgeben, wie oft die for-Schleife durchlaufen wurde.
Die Lösung findest du in ch_09. 
'''

from machine import Pin
import time, math
pause = 0.5
led = Pin("LED", Pin.OUT)

for i in range(1,201):
    led.toggle()
    time.sleep(pause)
    print(f"LED hat {math.ceil(i/2)}x geblinkt, Schaltperiode = {pause} Sekunden")
    pause = 0.9 * pause
    