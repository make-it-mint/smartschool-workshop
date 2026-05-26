'''
Ändere das Programm so, dass du anstatt die LED "on" und "off" zu schalten, den Zustand der LED änderst.
Also, dass sie aus geht, sollte sie an sein und sie an geht, sollte sie aus sein. Das ganze soll 100 Mal passieren.
Warum ist das für ein Programm sinnvoll einen "Pin" so zu steuern?
Die Lösung findest du in ch_08. 
'''

from machine import Pin
import time
pause = 0.5
led = Pin("LED", Pin.OUT)

for i in range(1,100):
    led.on()
    time.sleep(pause)
    led.off()
    time.sleep(pause)
    print(f"LED hat {i}x geblinkt, Blinkperiode = {pause*2} Sekunden")
    pause = 0.9 * pause
