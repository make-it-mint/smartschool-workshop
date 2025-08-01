from iot_settings import *
from Thing import Thing

#this class inherits all the functionalities of the "Thing" class. You can override specific methods according to your requirements
class CustomThing(Thing):
    def __init__(self,subscribe_topics):
        super().__init__(subscribe_topics)

    #################################################### This is where your custom code goes #######################################
    
    #overriding the selectAction method to react to the new topic and print the value
    def selectAction(self, topic, content):
        if topic == "my_test":
            print(f"Topic 1: {content}")
        elif topic == "test2":
            print(f"Topic 2: {content}")

    ###############################################################################################################################


#create an instance of the class with your custom topics
CustomThing(subscribe_topics=["my_test", "test2"]).start()

