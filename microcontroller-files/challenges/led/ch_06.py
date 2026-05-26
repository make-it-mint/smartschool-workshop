'''
Ändere das Programm so, dass das Blinken bei jedem Durchlauf der for-Schleife schneller wird und funktioniert,
egal wie viele Durchläufe die for-Schleife hat.
Die Lösung findest du in ch_07. 
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
    pause = 2*pause
