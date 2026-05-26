'''
Irgendwo in diesem Programm hat sich ein Fehler eingeschlichen, versuche ihn zu finden.
Ziel: Die LED soll 10x blinken.
Die Lösung findest du in ch_05. 
'''

from machine import Pin
import time
pause = 0.5
led = Pin("LED", Pin.OUT)

for i in range(1,10):
    led.on()
    time.sleep(pause)
    led.off()
    time.sleep(pause)
    print(f"LED hat {i}x geblinkt")
