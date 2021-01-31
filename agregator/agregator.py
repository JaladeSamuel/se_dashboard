#!/usr/bin/python
# -*- coding: latin-1 -*-

from sensor import Sensor
import numpy as np
import time

import json
import paho.mqtt.client as mqtt

class AbstractAgregator:
    def __init__(self,list_of_sensor,name,latitude,longitude):
        self.list_of_sensor = list_of_sensor 
        self.name = name # name of the agregator
        self.longitude = longitude
        self.latitude = latitude
        self.dic = {}

        
    def run_agregator(self):
        while True:

            # send in mqtt to the server
            client = mqtt.Client(client_id='publisher-1')  # Creating client
            client.connect("54.38.32.137",1883)  # Connect to broker
            ret = client.publish("/data_plouf/"+str(self.name)+"/gps",str(self.latitude)+" "+str(self.longitude))
            client.loop()

            for sensor in self.list_of_sensor:
                self.dic = {}
                self.dic["id"] = str(sensor.getid())
                self.dic["type"] = str(sensor.gettype()) 
                self.dic["localisation"] = str(sensor.getlocalisation())
                self.dic["value"] = sensor.getvalue()
                sensor.clear_buffer()
                print("buffer clear in sensor " + str(sensor.getid()))
                topic = "/data_plouf/"+str(self.name)+"/"+str(sensor.getid())

                #compute
                self.computation()

                # convert in Json
                dictionaryToJson = json.dumps(self.dic)
                print(topic,dictionaryToJson)
                ret = client.publish(topic,dictionaryToJson)
                # Run a loop
                client.loop()

            time.sleep(4) # TODO put 60 seconds

    
        
    def computation(self):
        # traiter les données et les enregistrés dans le dic
        raise NotImplementedError("do not call an abstract class bro !")


class Agregator_moyenne(AbstractAgregator):
    def __init__(self,list_of_sensor,name,latitude,longitude):
        AbstractAgregator.__init__(self,list_of_sensor,name,latitude,longitude)
        self.run_agregator()
        

    def computation(self):
        # traiter les données et les enregistrés dans le dic
        for key,value in self.dic.items():
            if key == "value":
                self.dic[key] = np.mean(value)
            


if __name__=="__main__":
    list_of_sensor = []
    print("c'est parti")
    temperature = Sensor("temp_ext","degre","Escalquens")
    pression_sensor = Sensor("hum","pression","Toulouse")
    humidite_sensor = Sensor("anemo","humidite","Labege")
    cpu_sensor = Sensor("temp_cpu","cpu vitesse","St Orens")

    list_of_sensor.append(temperature)
    list_of_sensor.append(pression_sensor)
    list_of_sensor.append(humidite_sensor)
    list_of_sensor.append(cpu_sensor)

    agregateur1 = Agregator_moyenne(list_of_sensor,"toulouse_agregator",43.604734392639955, 1.4435127815107553)
