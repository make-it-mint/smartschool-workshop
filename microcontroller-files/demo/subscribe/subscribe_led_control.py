from iot_settings import *
from thing import Thing
from snippets import *
from machine import Pin

#this class inherits all the functionalities of the "Thing" class. You can override specific methods according to your requirements
class CustomThing(Thing):
    def __init__(self,subscribe_topics):
        super().__init__(subscribe_topics)

    #################################################### This is where your custom code goes #######################################
    
    #overriding the selectAction method to react to the new topic and print the value
    def selectAction(self, topic, content, client):
        if topic == "demo/led_control":
            if content == "true":
                controlPin("LED", 1)
            elif content == "false":
                controlPin("LED", 0)
            client.publish("demo/led_state",f'getPinState("LED")')
            


    ###############################################################################################################################


#create an instance of the class with your custom topics
CustomThing(subscribe_topics=["demo/led_control"]).start()


