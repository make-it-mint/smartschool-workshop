from utime import sleep_ms
import sys
from machine import Pin
import network
import utime
import dht
from mqtt_simple import MQTTClient
from einstellungen import *

#SYSTEMEINSTELLUNGEN


#TOPICS
TOPIC_STATUS = 'KLASSE1/LUEFTUNG/STATUS'
TOPIC_TEMPERATUR = 'KLASSE1/LUFT/TEMP'
TOPIC_LUFTFEUCHTIGKEIT = 'KLASSE1/LUFT/FEUCHTE'

#SKRIPTVARIABLEN
MOTOR_AN = False
TEMP = 0
HUMID = 50
TEMP_GRENZWERT = 29
HUMID_GRENZWERT = 70

#GPIO PINS 
MOTOR = Pin(28, Pin.OUT)
LED_BLAU = Pin(13, Pin.OUT)
LED_GRUEN = Pin(17, Pin.OUT)
LED_ROT = Pin(14, Pin.OUT)
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


def my_callback(topic, nachricht):
    global MOTOR_AN, HUMID, TEMP
    #print((topic, nachricht))s
    try:
        #TEMPERATUR_GRENZWERT VERÄNDERN
        if topic.decode("utf-8") == TOPIC_TEMPERATUR:
            TEMP = float(nachricht)
            if MOTOR_AN and TEMP < TEMP_GRENZWERT and HUMID < HUMID_GRENZWERT:
                MOTOR_AN = False
                MOTOR.off()
            elif not MOTOR_AN and (TEMP >= TEMP_GRENZWERT or HUMID >= HUMID_GRENZWERT):
                MOTOR_AN = True
                MOTOR.on()
        elif topic.decode("utf-8") == TOPIC_LUFTFEUCHTIGKEIT:
            HUMID = float(nachricht)
            if MOTOR_AN and HUMID < HUMID_GRENZWERT and TEMP < TEMP_GRENZWERT:
                MOTOR_AN = False
                MOTOR.off()
            elif not MOTOR_AN and (HUMID >= HUMID_GRENZWERT or TEMP >= TEMP_GRENZWERT):
                MOTOR_AN = True
                MOTOR.on()

        LED_BLAU.on() if MOTOR_AN else LED_BLAU.off()
        client.publish(TOPIC_STATUS, msg=f'{MOTOR_AN}')

    except Exception as e:
        print(e)

try:
    client = mqtt_connect()
except OSError as e:
    print("Verbindung mit MQTT Broker konnte nicht hergestellt werden")
    sys.exit()



client.publish(TOPIC_STATUS, msg=f'{MOTOR_AN}')
#Subscription Topics auswählen
client.subscribe(TOPIC_TEMPERATUR)
client.subscribe(TOPIC_LUFTFEUCHTIGKEIT)
LED_STATUS.on()

while True:
    #Überprüfen ob neue Inhalte auf den subcribed Topics geschickt wurden
    client.check_msg()
    utime.sleep(.1)
        
        
        




