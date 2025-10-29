from machine import Pin, I2C, PWM, ADC
from utime import sleep, sleep_us, ticks_us
from machine_i2c_lcd import I2cLcd
import dht
import math
import neopixel



def controlLed(led_pin=16,set_to=-1):
    my_pin = Pin(led_pin, Pin.OUT)
    if set_to == -1:
        my_pin.toggle()
    elif set_to == 0:
        my_pin.off()
    elif set_to == 1:
        my_pin.on()


def waitForButtonPress(button_pin=15):
    my_pin = Pin(button_pin, Pin.IN, Pin.PULL_DOWN)
    while my_pin.value() == 0:
        sleep(.1)
    return button_pin

#https://thepihut.com/blogs/raspberry-pi-tutorials/micropython-skill-builders-11-keypads?srsltid=AfmBOoq0VMqkxMMrefxU5ckmVZsXh4VxV-30n4ZqcCWFRtN2kKWcBLg8
def sendKeyPadMessage(row_pins=[13, 12, 11, 10], col_pins=[9, 8, 7, 6], send_key = "*"):
    #         C0   C1   C2   C3
    keys = [['1', '2', '3', 'A'], # R0
            ['4', '5', '6', 'B'], # R1
            ['7', '8', '9', 'C'], # R2
            ['*', '0', '#', 'D']] # R3
    
    for idx in range(len(row_pins)):
        # Rows are OUTPUTs which we set HIGH or LOW
        row_pins[idx] = Pin(row_pins[idx], Pin.OUT, value = 0)
        # Columns are INPUTS with internal PULL_DOWNS
        col_pins[idx] = Pin(col_pins[idx], Pin.IN, Pin.PULL_DOWN)
    text = ""
    while True:
        for row_idx,row in enumerate(row_pins):
            row.high()
            for col_idx,col in enumerate(col_pins):
                if col.value() == 1:
                    key = keys[row_idx][col_idx]
                    if key == send_key:
                        row.low()
                        return text
                    else:
                        text+= key
                        sleep(.3)
                        print(text)
                        break
            row.low()

#https://microcontrollerslab.com/raspberry-pi-pico-rfid-rc522-micropython/
def readRFID(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0):
    reader = MFRC522(spi_id=spi_id, sck=sck, miso=miso, mosi=mosi, cs=cs, rst=rst)

    print("Bring TAG closer...")
    print("")
    while True:
        reader.init()
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card = int.from_bytes(bytes(uid),"little",False)
                return str(card)
        sleep(.2)


#https://www.elektronik-kompendium.de/sites/raspberry-pi/2612251.htm
def writeLCD(sda_pin=20, sdc_pin=21, text="", delay = True):
    # Initialisierung I2C
    i2c = I2C(0, sda=Pin(sda_pin), scl=Pin(sdc_pin), freq=100000)
    # Initialisierung LCD über I2C
    lcd = I2cLcd(i2c, 0x27, 2, 16)

    # Display-Zeilen ausgeben    
    current_character = 0
    zeile = 0
    while current_character < len(text):
        if current_character > 15:
            zeile = 1
        if current_character%16 == 0 and current_character>0:
            if not delay:
                sleep(2)
            lcd.clear()
            lcd.putstr(text[current_character-16:current_character])
        lcd.move_to(current_character%16, zeile)
        lcd.putstr(text[current_character])
        if delay:
            sleep(.1)
        current_character += 1
    sleep(2)
    lcd.clear()
    lcd.backlight_off()


#https://www.elektronik-kompendium.de/sites/raspberry-pi/2703031.htm
def readDTH22(data_pin=15, get_temp=True, get_hum=True):
    sensor = dht.DHT22(Pin(data_pin, Pin.IN, Pin.PULL_UP))
    sensor.measure()
    if get_temp and not get_hum:
        return sensor.temperature()
    elif get_temp and get_hum:
        return sensor.temperature(),sensor.humidity()
    elif not get_temp and get_hum:
        return sensor.humidity()
    elif not get_temp and not get_hum:
        return None


#https://www.elektronik-kompendium.de/sites/raspberry-pi/2612221.htm
def readLDR(ldr_pin=26):
    ldr = ADC(ldr_pin)
    max_brightness=65535
    return round(ldr.read_u16()/max_brightness,2)

def buzz():
    pass


def controlMotorDC(in1_pin=16, in2_pin=17, speed=100, direction=1):
    frequency = 1000
    #duty_cycle (0-65535)
    lower_bound = 65535*0.3 #30%
    duty_cycle_multiplier =(65535-lower_bound)/100
    in1= PWM(Pin(in1_pin))
    in2= PWM(Pin(in2_pin))
    in1.freq(frequency)
    in2.freq(frequency)
    if direction == 1:
        in1.duty_u16(int(speed*duty_cycle_multiplier+lower_bound))
        in2.duty_u16(0)
    elif direction == 0:
        in1.duty_u16(0)
        in2.duty_u16(0)
    elif direction == -1:
        in1.duty_u16(0)
        in2.duty_u16(int(speed*duty_cycle_multiplier+lower_bound))
    
    

def readMotionSensor(pir_pin=16):
    sensor=Pin(pir_pin, Pin.IN, Pin.PULL_DOWN)
    if sensor.value():
        return True
    else:
        return False

#https://www.elektronik-kompendium.de/sites/raspberry-pi/2701131.htm
def readUltrasound(echo_pin=17, trig_pin=16, v_schall=343.2):
    trigger = Pin(trig_pin, Pin.OUT)
    echo = Pin(echo_pin, Pin.IN)

    #Impuls senden
    trigger.low()
    sleep_us(2)
    trigger.high()
    sleep_us(5)
    trigger.low()
    
    # Zeitmessungen
    while echo.value() == 0:
       signal_off = ticks_us()
    while echo.value() == 1:         
       signal_on = ticks_us()
    # Vergangene Zeit ermitteln
    dauer = signal_on - signal_off
    # Abstand/Entfernung ermitteln
    # Entfernung über die Schallgeschwindigkeit (343.2 m/s bei 20 °C) berechnen
    # Durch 2 teilen, wegen Hin- und Rückweg. Durch 1.000 teilen, wegen Mikrosekunden
    # Multiplizieren mit 100 für Centimeret
    abstand = dauer * v_schall*100 / (2*1000000)
    return abstand

#https://www.elektronik-kompendium.de/sites/raspberry-pi/2706231.htm
def writeServo(data_pin=16, position_grad=90):
    servo = PWM(Pin(data_pin))
    servo.freq(50)
    if position_grad > 180 or position_grad < 0:
        servo.deinit()
        return False
    else:
        position = int(math.ceil(2000000*position_grad/180 + 500000))
        servo.duty_ns(position)
        sleep(2)
        return True
    pass

#https://www.elektronik-kompendium.de/sites/raspberry-pi/2802011.htm
def readIR(data_pin=16):
    sensor = Pin(data_pin, Pin.IN, Pin.PULL_UP)
    #0 = objekt erfasst, 1 = kein Objekt
    return sensor.value()


def pixelstick(data_pin=28,pixel=[[0,0,0]]):
    np = neopixel.NeoPixel(Pin(data_pin),len(pixel))
    for i,p in enumerate(pixel):
        np[i] = p
    np.write()

#https://docs.sunfounder.com/projects/umsk/de/latest/04_pi_pico/pico_lesson02_soil_moisture.html
def readGroundMoisture(data_pin=26):
    sensor = ADC(data_pin)
    #65535 is der Maximalwert für 16bit integer
    return round(sensor.read_u16()/65535,2)

 #https://docs.sunfounder.com/projects/umsk/de/latest/04_pi_pico/pico_lesson02_soil_moisture.html
def controlRelais(relais_pin=16, set_to=True):
    relais = Pin(relais_pin, Pin.OUT)
    if set_to == True:
        relais.on()
    elif set_to == False:
        relais.off()
    return set_to
    
if __name__ == "__main__":
    while True:
        print(controlLed())
        sleep(3)
        