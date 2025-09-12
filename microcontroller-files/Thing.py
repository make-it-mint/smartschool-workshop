import machine,sys,json
import network
import utime
from umqtt.simple import MQTTClient
from iot_settings import *


class Thing:

    def __init__(self, subscribe_topics=[CLIENT_ID], status_led = "LED", loop_pause_in_ms = 200):
        self.STATUS_LED = machine.Pin(status_led, machine.Pin.OUT, value = 0)
        self.SUBSCRIBE_LIST = subscribe_topics
        self.PUBLISH_LIST = []
        self.LOOP_PAUSE_IN_MS = loop_pause_in_ms


    def setupConnection(self, led):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(SSID,WLAN_PWD)

        #quick blinking while trying to connect to wifi
        while not wlan.isconnected() and wlan.status() >= 0:
            led.toggle()
            utime.sleep(.2)

        #turn LED off after wifi was connected while trying to connect to the Broker
        led.off()
        
        client = self.connectClient()
        
        #LED on after broker is connected
        led.on()

        return client
    
    def connectClient(self):
        try:
            client = MQTTClient(client_id=CLIENT_ID, server=BROKER_IP, port = PORT, keepalive=60, user=USER, password=USER_PWD)
            client.set_callback(self.thingCallback)
            client.connect()
            #set all defined subscriptions
            client = self.setSubscriptions(client)
        except OSError as e:
            print(f"Broker Connection Error: {e}")
            self.STATUS_LED.off()
            sys.exit() #stop program if broker is not available
            
        return client
    
    def setSubscriptions(self, client):
        for topic in self.SUBSCRIBE_LIST:
            client.subscribe(topic)
            print(f"subscribed to {topic}")
        return client

    #by default nothing is published
    def publish(self, client):
        #example for publishing
        #client.publish("TOPIC_NAME","MESSAGE AS STRING")
        pass
           

    #this method is called if a message is received on a subscribed topic
    def thingCallback(self, topic, content):
        #checks if topic really is in subscription list and checks if it can be decoded
        if topic.decode("utf-8") in self.SUBSCRIBE_LIST:
            try:
                content = content.decode("utf-8")
                self.selectAction(topic.decode("utf-8"), content, self.client)
            except Exception as e:
                print(e)

    #if decoding was successful, depending on the received message and topic, an action can be selected
    #CHANGE THIS METHOD IN YOUR CUSTOM CLASS
    def selectAction(self, topic, content, client):
        #choose your action depending on the received topic
        if topic == CLIENT_ID:
            #call your custom method
            self.startActionTest(content)
        #add multiple different actions depending on the number of topics you subscribed to
        elif topic == "test2":
            pass
        else:
            pass

    #exmaple action method
    def startActionTest(self, content):
        #in this example the content of the message is printed to the console
        print(content)

    
    #This is the main loop, change it according to your requirements if necessary.
    #it is an endless loop that automatically reconnect to the broker, if the connection should ever break off.
    #this generally happens after no messages were sent or received during the specified timeout.
    def start(self):
        #connect to the Broker
        self.client = self.setupConnection(self.STATUS_LED)
        while True:
            print("connection successful")
            while True:
                try:
                    self.client.check_msg() # none blocking checking for messages on every loop
                    self.publish(self.client) # publish on every loop
                    utime.sleep_ms(self.LOOP_PAUSE_IN_MS) #pause for specified duration
                except Exception as e:
                    print(f"Broker connection terminated: {e}") #if broker should disconnect
                    break
                
            print("reconnecting Broker")
            self.client = self.connectClient()#automatically isconnects if Broker does not connect

            






