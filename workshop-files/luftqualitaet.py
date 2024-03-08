from utime import sleep_ms
import sys
from machine import Pin
import network
import utime
import dht
from umqtt.simple import MQTTClient
from einstellungen import *

#SYSTEMEINSTELLUNGEN


#TOPICS
TOPIC_STATUS = 'KLASSE1/LUFT/STATUS'
TOPIC_TEMPERATUR = 'KLASSE1/LUFT/TEMP'
TOPIC_LUFTFEUCHTIGKEIT = 'KLASSE1/LUFT/FEUCHTE'

#SKRIPTVARIABLEN
STATUS = True

#GPIO PINS
LED = Pin("LED", Pin.OUT)
DHT = dht.DHT22(Pin(19))


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
    sys.exit()



client.publish(TOPIC_STATUS, msg=f'{STATUS}')
client.disconnect()
LED.on()
 
while True:

    try:
        DHT.measure()
        temp = DHT.temperature()
        hum = DHT.humidity()
        client = mqtt_connect()
        client.publish(TOPIC_TEMPERATUR, msg=f'{temp}')
        client.publish(TOPIC_LUFTFEUCHTIGKEIT, msg=f'{hum}')
        client.disconnect()
        print('Temperature: %3.1f C' %temp)
        #print('Humidity: %3.1f %%' %hum)
    except OSError as e:
        print('Failed to read sensor.')
    
    sleep_ms(500)

STATUS = False
client = mqtt_connect()
client.publish(TOPIC_STATUS, msg=f'{STATUS}')
client.disconnect()
LED.off()
        
        




