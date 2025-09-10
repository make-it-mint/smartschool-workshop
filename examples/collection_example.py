from iot_settings import *
from Thing import Thing
from things_collection import * #import all functions from the things_collection module. Module needs to be copied to microcontroller

#this class inherits all the functionalities of the "Thing" class. You can override specific methods according to your requirements
class CustomThing(Thing):
    def __init__(self):
        super().__init__()

    #################################################### This is where your custom code goes #######################################
    
    #overriding the publish method
    def publish(self, client):
        #waiting for a button to be pressed. The return value is the Pin ID of the button. Default value can be viewed or adjusted in "things_collection" module
        value = waitForButtonPress()
        #publish to specified topic
        client.publish("my_test_topic", f"Button Pin: {value}")

    ###############################################################################################################################
#this instance automatically subscribes to the topic that is equal to the "CLIENT_ID" value set in iot_settings
Thing().start()
