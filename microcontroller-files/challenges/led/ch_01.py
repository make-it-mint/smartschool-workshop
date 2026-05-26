'''
Irgendwo in diesem Programm hat sich ein Fehler eingeschlichen, versuche ihn zu finden.
Ziel: Die LED soll langsam blinken.
Die Lösung findest du in ch_02. 
'''

import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.on()
    time.sleep(1)
    led.off()
