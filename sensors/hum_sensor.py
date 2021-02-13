from sensor import MetaSensor
import paho.mqtt.client as mqtt
import random
import time
import sys

class hum_sensor(MetaSensor):
    
    __metaclass__ = MetaSensor
    def __init__(self, id, type):
        super().__init__(id, type)
    
    def get_value(self):
        return random.randint(30, 60)
         

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("Error missing arg : hum_sensor.py [city_name]")
    rasp_hum = hum_sensor(str(sys.argv[1]),"percentage")
    # Creating client
    client = mqtt.Client()
    # Connect to broker
    client.connect("localhost")
    
    while(True):
        # Get value sensor
        msg = rasp_hum.get_value()
        # Publish a temperature value
        ret = client.publish("/" + str(rasp_hum.id) + "/hum_sensor", msg)
        # Run a loop
        client.loop()
        time.sleep(1)
        
        