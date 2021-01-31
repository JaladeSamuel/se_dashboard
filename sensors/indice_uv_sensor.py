from sensor import MetaSensor
import paho.mqtt.client as mqtt
import random
import time

class indice_uv_sensor(MetaSensor):
    
    __metaclass__ = MetaSensor
    def __init__(self, id, type):
        super().__init__(id, type)
    
    def get_value(self):
        return random.randint(10, 15)
         

if __name__ == '__main__':
    rasp_indice_uv = indice_uv_sensor("toulouse","uv")
    # Creating client
    client = mqtt.Client(client_id="uv_sensor")
    # Connect to broker
    client.connect("localhost")
    
    while(True):
        # Get value sensor
        msg = rasp_indice_uv.get_value()
        # Publish a temperature value
        ret = client.publish("/" + rasp_indice_uv.id + "/indice_uv_sensor", msg)
        # Run a loop
        client.loop()
        time.sleep(5)
        
        