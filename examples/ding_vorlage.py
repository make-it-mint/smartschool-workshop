import machine,sys
import network
import utime
from umqtt.simple import MQTTClient
from einstellungen import *

#SYSTEMEINSTELLUNGEN


#TOPICS
TOPIC_PUBLISHING = 'HEAD_TOPIC/FROM_MC'
TOPIC_SUBSCRIPTION = 'HEAD_TOPIC/TO_MC'

#SKRIPTVARIABLEN
LED_BLINKFREQUENZ_IN_HERTZ = 1
PUBLISHING_INTERVALL_IN_SEKUNDEN = 5

#GPIO PINS 
led = machine.Pin("LED", machine.Pin.OUT)


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
    #PUBLISHING Beispiel Broker: mosquitto_pub -h localhost -t "HEAD_TOPIC/TO_MC" -m "2:6"
    #Format:     BLINKING_FREQUENCY_HZ:PUBLISHING_INTERVAL_S
    global LED_BLINKFREQUENZ_IN_HERTZ, PUBLISHING_INTERVALL_IN_SEKUNDEN
    print((topic, nachricht))
    if topic.decode("utf-8") == TOPIC_SUBSCRIPTION:
        try:
            nachricht = nachricht.decode("utf-8")
            werte = nachricht.split(":")
            LED_BLINKFREQUENZ_IN_HERTZ=int(werte[0])
            PUBLISHING_INTERVALL_IN_SEKUNDEN=int(werte[1])
        except Exception as e:
            print(e)


try:
    client = mqtt_connect()
except OSError as e:
    print("Verbindung mit MQTT Broker konnte nicht hergestellt werden")
    sys.exit()

client.subscribe(TOPIC_SUBSCRIPTION) 
zuletzt_published_zeit=utime.ticks_ms()

while True:
    client.check_msg()
    if utime.ticks_diff(utime.ticks_ms(),zuletzt_published_zeit)/1000 > PUBLISHING_INTERVALL_IN_SEKUNDEN:
        client.publish(TOPIC_PUBLISHING, msg=f'MEIN WERT')
        print("PUBLISHED")
        zuletzt_published_zeit=utime.ticks_ms()
    else:
        print(utime.ticks_diff(utime.ticks_ms(),zuletzt_published_zeit)/1000)

    led.on()
    utime.sleep(1/(LED_BLINKFREQUENZ_IN_HERTZ*2))
    led.off()
    utime.sleep(1/(LED_BLINKFREQUENZ_IN_HERTZ*2))