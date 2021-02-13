from sensor import MetaSensor
import paho.mqtt.client as mqtt
import numpy as np
import time
import sys

class temp_ext_sensor(MetaSensor):
    
    __metaclass__ = MetaSensor
    def __init__(self, id, type):
        super().__init__(id, type)
    
    def get_value(self):
        temperature_ext = 19.5 + np.random.rand()
        return temperature_ext

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("Error missing arg : temp_ext_sensor.py [city_name]")
    rasp_temp_ext = temp_ext_sensor(str(sys.argv[1]),"degree")

    # Creating client
    client = mqtt.Client()
    # Connect to broker
    client.connect("localhost")
    
    while(True):
        # Get value sensor
        msg = rasp_temp_ext.get_value()
        # Publish a temperature value
        ret = client.publish("/" + str(rasp_temp_ext.id) + "/temp_ext_sensor", msg)
        # Run a loop
        client.loop()
        time.sleep(1)
        
        