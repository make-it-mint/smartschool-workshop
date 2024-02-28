from utime import sleep_ms
import sys
from machine import Pin, ADC
import network
import utime
import dht
from mqtt_simple import MQTTClient
from einstellungen import *

#SYSTEMEINSTELLUNGEN


#TOPICS
TOPIC_STATUS = 'KLASSE1/LICHT/STATUS'
TOPIC_HELLIGKEIT = 'KLASSE1/LICHT/HELLIGKEIT'
TOPIC_BEWEGUNG = 'KLASSE1/LICHT/BEWEGUNG'
TOPIC_STATUS_HELLIGKEIT = 'KLASSE1/LICHT/STATUS_HELLIGKEIT'
TOPIC_STATUS_BEWEGUNG = 'KLASSE1/LICHT/STATUS_BEWEGUNG'

#SKRIPTVARIABLEN
LICHT_AN = False

HELLIGKEIT_GRENZWERT = 0.5
HELLIGKEIT = 0.0
BEWEGUNG = False
BEWEGUNG_AKTIV = True
HELLIGKEIT_AKTIV = True

#GPIO PINS
PIR = Pin(18, Pin.IN, Pin.PULL_DOWN)
LDR = ADC(0)
LED_LICHT = Pin(16, Pin.OUT)
LED_STATUS = Pin("LED", Pin.OUT)

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

def helligkeit_messen():
    #Gibt einen Helligkeitswert zwischen 0 und 1 zurück. z.B. 0.15 oder 0.3
    #Der Wert steigt mit zunehmender Helligkeit
    return round((1-int(LDR.read_u16())/65535),2)


def my_callback(topic, nachricht):
    global BEWEGUNG_AKTIV, HELLIGKEIT_AKTIV
    #print((topic.decode("utf-8"), nachricht.decode("utf-8")))
    try:
        #LED per Topic an und aus schalten
        if topic.decode("utf-8") == TOPIC_STATUS_HELLIGKEIT:
            HELLIGKEIT_AKTIV = True if nachricht.decode("utf-8") == "True" else False
            
        elif topic.decode("utf-8") == TOPIC_STATUS_BEWEGUNG:
            BEWEGUNG_AKTIV = True if nachricht.decode("utf-8") == "True" else False
            


    except Exception as e:
        print(e)

try:
    client = mqtt_connect()
except OSError as e:
    print("Verbindung mit MQTT Broker konnte nicht hergestellt werden")
    sys.exit()


client.publish(TOPIC_STATUS, msg=f'{LICHT_AN}')
client.publish(TOPIC_STATUS_HELLIGKEIT, msg=f'{HELLIGKEIT_AKTIV}')
client.publish(TOPIC_STATUS_BEWEGUNG, msg=f'{BEWEGUNG_AKTIV}')


client.subscribe(TOPIC_STATUS_HELLIGKEIT)
client.subscribe(TOPIC_STATUS_BEWEGUNG)


LED_STATUS.on()

while True:
    #Überprüfen ob neue Inhalte auf den subcribed Topics geschickt wurden
    client.check_msg()

    HELLIGKEIT = helligkeit_messen()
    BEWEGUNG = bool(PIR.value())
    
    if HELLIGKEIT_AKTIV and not BEWEGUNG_AKTIV:
        if HELLIGKEIT <= HELLIGKEIT_GRENZWERT and not LICHT_AN:
                LICHT_AN = True
                LED_LICHT.on()
        elif HELLIGKEIT > HELLIGKEIT_GRENZWERT and LICHT_AN:
            LICHT_AN = False
            LED_LICHT.off()
    
    
    elif not HELLIGKEIT_AKTIV and BEWEGUNG_AKTIV:
        if BEWEGUNG and not LICHT_AN:
                LICHT_AN = True
                LED_LICHT.on()
        elif not BEWEGUNG and LICHT_AN:
            LICHT_AN = False
            LED_LICHT.off()
            
            
    elif HELLIGKEIT_AKTIV and BEWEGUNG_AKTIV:
        if (BEWEGUNG or HELLIGKEIT <= HELLIGKEIT_GRENZWERT) and not LICHT_AN:
                LICHT_AN = True
                LED_LICHT.on()
        elif (not BEWEGUNG and HELLIGKEIT > HELLIGKEIT_GRENZWERT) and LICHT_AN:
            LICHT_AN = False
            LED_LICHT.off()
            
    client.publish(TOPIC_HELLIGKEIT, msg=f'{HELLIGKEIT}')
    client.publish(TOPIC_BEWEGUNG, msg=f'{BEWEGUNG}')
    client.publish(TOPIC_STATUS, msg=f'{LICHT_AN}')
    
    utime.sleep(1)
        
        
        





