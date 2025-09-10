from machine import Pin
from utime import sleep
from mfrc522 import MFRC522



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



def readDTH11():
    pass

def readLDR():
    pass

def buzz():
    pass

def writeLCD():
    pass

def readLCD():
    pass

def controlStepper():
    pass

def controlMotorDC():
    pass

def readMotionSensor():
    pass

def readUltrasound():
    pass

def readServo():
    pass

def writeServo():
    pass

def readIR():
    pass

def writeIR():
    pass


if __name__ == "__main__":
    while True:
        print(sendKeyPadMessage())
        sleep(1)