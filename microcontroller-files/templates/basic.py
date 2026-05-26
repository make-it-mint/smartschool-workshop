from iot_settings import *
from thing import Thing


#this instance automatically subscribes to the topic that is equal to the "CLIENT_ID" value set in iot_settings
Thing().start()
