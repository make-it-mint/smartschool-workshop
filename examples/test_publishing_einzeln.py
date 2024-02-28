import machine, sys
import network
import utime
from umqtt.simple import MQTTClient
from einstellungen import *
#TOPICS
TOPIC_PUBLISHING = 'MEINE_TOPIC/TESTS/EINZELN_PUBLISH'

#SKRIPTVARIABLEN
MEIN_TEXT = "MEIN TEXT HIER"


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID,PASSWORT)

while not wlan.isconnected() and wlan.status() >= 0:
	print("Verbinde...")
	utime.sleep(1)




def mqtt_connect():
    client = MQTTClient(CLIENT_ID, BROKER_IP, keepalive=60)
    client.connect()
    print(f'Mit dem MQTT Broker auf IP: {BROKER_IP} verbunden')
    return client


try:
    client = mqtt_connect()
    client.publish(TOPIC_PUBLISHING, msg=MEIN_TEXT)
except OSError as e:
    print("Verbindung mit MQTT Broker konnte nicht hergestellt werden")
    sys.exit()

