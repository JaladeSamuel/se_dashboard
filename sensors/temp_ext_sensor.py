from sensor import MetaSensor
import paho.mqtt.client as mqtt
import numpy as np
import time

class temp_ext_sensor(MetaSensor):
    
    __metaclass__ = MetaSensor
    def __init__(self, id, type, latitude, longitude):
        super().__init__(id, type, latitude, longitude)
    
    def get_value(self):
        temperature_ext = 19.5 + np.random.rand()
        return temperature_ext

if __name__ == '__main__':
    rasp_temp_ext = temp_ext_sensor(0,'float', 43.56079970371226, 1.4602410389826976)
    # Creating client
    client = mqtt.Client(client_id='temp_ext_sensor')
    # Connect to broker
    client.connect("localhost")
    
    while(True):
        # Get value sensor
        msg = rasp_temp_ext.get_value()
        gps = (rasp_temp_ext.latitude, rasp_temp_ext.longitude)
        # Publish a temperature value
        ret = client.publish("/" + str(rasp_temp_ext.id) + "/temp_ext_sensor", msg)
        # Publish a GPS value
        ret = client.publish("/" + str(rasp_temp_ext.id) + "/gps", gps)
        # Run a loop
        client.loop()
        time.sleep(5)
        
        