'''
Irgendwo in diesem Programm hat sich ein Fehler eingeschlichen, versuche ihn zu finden.
Ziel: Die LED soll 1 Mal pro Sekunde blinken. Also eine Blinkperiode (An und Aus) hat eine Dauer von einer Sekunde
Die Lösung findest du in ch_03.
'''

import machine
import time
pause = 1
led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.on()
    time.sleep(pause)
    led.off()
    time.sleep(pause)
