'''
Ändere das Programm so, dass das Blinken bei jedem Durchlauf der for-Schleife langsamer wird und unendlich weiter wachsen kann.
Teste dein Programm mit 100 Durchläufen der for-Schleife.
Eine Lösung findest du in ch_06. 
'''

from machine import Pin
import time
pause = 0.5
led = Pin("LED", Pin.OUT)

for i in range(1,11):
    led.on()
    time.sleep(pause)
    led.off()
    time.sleep(pause)
    print(f"LED hat {i}x geblinkt, Blinkperiode = {pause*2} Sekunden")
