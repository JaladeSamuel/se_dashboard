import os
from sensors.sensor import MetaSensor
import numpy as np
import paho.mqtt.client as mqtt

class OrelSensor(MetaSensor):
    _metaclass__ = MetaSensor
    
    def __init__(self, id, name):
        super().__init__(id,name)
        
    def getvalue(self):
        return self.get_memory_usage()
    
    def getimg(self):
        os.system("node svgtojson.js image.svg")
        
    

if __name__ == '__main__':
    orelsensor = OrelSensor(0,'json')
    # Creating client
    client = mqtt.Client(client_id='orelsensor')

    # Connect to broker
    client.connect("54.38.32.137",1883)
    
    # Get value sensor
    msg = orelsensor.getimg()

    # Publish a message with topic
    ret= client.publish("data/orelsensor",msg)

    # Run a loop
    client.loop()