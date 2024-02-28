import machine, sys
import network
import utime
from umqtt.simple import MQTTClient
from einstellungen import *

#TOPICS
TOPIC_SUBSCRIPTION = 'MEINE_TOPIC/TESTS/SUBSCRIBE'


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID,PASSWORT)

while not wlan.isconnected() and wlan.status() >= 0:
	print("Verbinde...")
	utime.sleep(1)




def mqtt_connect():
    client = MQTTClient(CLIENT_ID, BROKER_IP, keepalive=60)
    client.set_callback(my_callback)
    client.connect()
    print(f'Mit dem MQTT Broker auf IP: {BROKER_IP} verbunden')
    return client


def my_callback(topic, nachricht):
    if topic.decode("utf-8") == TOPIC_SUBSCRIPTION:
        try:
            nachricht = nachricht.decode("utf-8")
            print(nachricht)
        except Exception as e:
            print(e)


try:
    client = mqtt_connect()
except OSError as e:
    print("Verbindung mit MQTT Broker konnte nicht hergestellt werden")
    sys.exit()

client.subscribe(TOPIC_SUBSCRIPTION) 

while True:
    print("Überprüfe TOPIC")
    client.check_msg()
    utime.sleep(1)
    