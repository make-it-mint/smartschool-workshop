from iot_settings import *
from thing import Thing
from snippets import *

#this class inherits all the functionalities of the "Thing" class. You can override specific methods according to your requirements
class CustomThing(Thing):
    def __init__(self):
        super().__init__()

    #################################################### This is where your custom code goes ######################################
    #overriding the publish method
    def publish(self, client):
        #sned key is "*"
        client.publish("demo/keypad", f"{sendKeyPadMessage()}")

    ###############################################################################################################################


#create an instance of the class, since you do not subscribe to any custom topics with this device, no topics need to be set
CustomThing().start()
