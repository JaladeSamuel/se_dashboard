from sensor import MetaSensor
import paho.mqtt.client as mqtt
import random
import time

class anemo_sensor(MetaSensor):
    
    __metaclass__ = MetaSensor
    def __init__(self, id, type):
        super().__init__(id, type)
    
    def get_value(self):
        return random.randint(30, 40)
         

if __name__ == '__main__':
    rasp_anemo = anemo_sensor("toulouse",'km/h')
    # Creating client
    client = mqtt.Client()
    # Connect to broker
    client.connect("localhost")
    
    while(True):
        # Get value sensor
        msg = rasp_anemo.get_value()
        # Publish a temperature value
        ret = client.publish("/" + str(rasp_anemo.id) + "/anemo_sensor", msg)
        # Run a loop
        client.loop()
        time.sleep(1)
        
        