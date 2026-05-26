'''
Irgendwo in diesem Programm hat sich ein Fehler eingeschlichen, versuche ihn zu finden.
Ziel: Die LED soll 1 Mal pro Sekunde blinken. Also eine Blinkperiode (An und Aus) hat eine Dauer von einer Sekunde
Die Lösung findest du in ch_03. 
'''

from machine import pin
import time
pause = 0.5
led = pin("LED", pin.OUT)

while True:
    led.on()
    time.sleep(pause)
    led.off()
    time.sleep(pause)
