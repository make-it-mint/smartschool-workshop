'''
Super, du hast jetzt eine Funktion mit der du einstellen kannst, wie oft deine LED blinkt und kannst diese Funktion flexibel in einem Programm verwenden.
Man könnte noch weitere Argumente nutzen, um die Funktion noch flexibler zu nutzen. Welche sind das? Setze sie ein.
Die Lösung findest du in ch_11. 
'''

from machine import Pin
import time, math


def led_blinken(num_loops):
    pause = 0.5
    led = Pin("LED", Pin.OUT)
    for i in range(1,num_loops+1):
        led.toggle()
        time.sleep(pause)
        print(f"LED hat {math.ceil(i/2)}x geblinkt, Schaltperiode = {pause} Sekunden")
        pause = 0.9 * pause
    return i

print(led_blinken(num_loops=100))
