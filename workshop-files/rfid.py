from utime import sleep_ms
from mfrc522 import MFRC522
import machine,sys
import network
import utime
from umqtt.simple import MQTTClient
from einstellungen import *

#SYSTEMEINSTELLUNGEN


#TOPICS
TOPIC_PUBLISHING = 'KLASSE1/ERFASSUNG'

#SKRIPTVARIABLEN
ANWESENDE=[]

#GPIO PINS 
rot = machine.Pin(14, machine.Pin.OUT)
gruen = machine.Pin(13, machine.Pin.OUT)
pieper = machine.Pin(15, machine.Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID,PASSWORT)

while not wlan.isconnected() and wlan.status() >= 0:
	print("Verbinde...")
	utime.sleep(1)




def mqtt_connect():
    client = MQTTClient(CLIENT_ID, BROKER_IP, port=1883, keepalive=60)
    client.set_callback(my_callback)
    client.connect()
    print(f'Mit dem MQTT Broker auf IP: {BROKER_IP} verbunden')
    return client


def my_callback(topic, nachricht):

    pass

try:
    client = mqtt_connect()
except OSError as e:
    print("Verbindung mit MQTT Broker konnte nicht hergestellt werden")
    rot.on()
    pieper.on()
    sleep_ms(1000)
    pieper.off()
    rot.off()
    sys.exit()

reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)


client.publish(TOPIC_PUBLISHING, msg=f'Online')
client.disconnect()

 
while True:

    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            client.connect()
            if str(card) in ANWESENDE:
                ANWESENDE.remove(str(card))  
                client.publish(TOPIC_PUBLISHING, msg=f'{str(card)} ist gegangen')
                rot.on()
                pieper.on()
                sleep_ms(200)
                pieper.off()
                sleep_ms(200)
                pieper.on()
                sleep_ms(200)
                pieper.off()
                sleep_ms(1400)
                rot.off()
            elif not str(card) in ANWESENDE:
                ANWESENDE.append(str(card))
                client.publish(TOPIC_PUBLISHING, msg=f'{str(card)} ist anwesend')
                gruen.on()
                pieper.on()
                sleep_ms(500)
                pieper.off()
                sleep_ms(1500)
                gruen.off()
            client.disconnect()
            
    sleep_ms(500) 
