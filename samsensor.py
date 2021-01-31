from sensors.sensor import MetaSensor
import numpy as np
import paho.mqtt.client as mqtt

class SamSensor(MetaSensor):
    
    __metaclass__ = MetaSensor
    def __init__(self, id, name):
        super().__init__(id,name)
    
    def getvalue(self):
        return np.random.random_sample()
    

if __name__ == '__main__':
    rasp = SamSensor(0,'float')
    # Creating client
    client = mqtt.Client(client_id='samsensor')

    # Connect to broker
    client.connect("54.38.32.137",1883)
    
    # Get value sensor
    msg = rasp.getvalue()

    # Publish a message with topic
    ret= client.publish("data/samsensor",str(msg))

    # Run a loop
    client.loop_forever()
        