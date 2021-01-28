#!/usr/bin/python
# -*- coding: latin-1 -*-

from sensor import Sensor
import numpy as np
import time

import json
#import paho.mqtt.client as paho

class AbstractAgregator:
    def __init__(self,list_of_sensor):
        self.list_of_sensor = list_of_sensor 
        self.dic = {}
        
    def run_agregator(self):
        while True:
            # update data 
            for sensor in self.list_of_sensor: 
                name = str(sensor.getid()) + " - " + str(sensor.gettype()) + " - " + str(sensor.getlocalisation())
                self.dic[name] = sensor.getvalue()

            # compute 
            self.computation()
            # send to the server 
            print(self.send_mqtt())
            
            for sensor in self.list_of_sensor:
                sensor.clear_buffer()
                print("buffer clear in sensor " + str(sensor.getid()))

            time.sleep(4) # TODO put 60 seconds

    
        
    def computation(self):
        # traiter les données et les enregistrés dans le dic
        raise NotImplementedError("do not call an abstract class bro !")
        
    
    def send_mqtt(self):
        # convert in Json
        dictionaryToJson = json.dumps(self.dic)
        return dictionaryToJson
        # send in mqtt
    
    

class Agregator_moyenne(AbstractAgregator):
    def __init__(self,cote):
        AbstractAgregator.__init__(self,list_of_sensor)
        self.run_agregator()
        

    def computation(self):
        # traiter les données et les enregistrés dans le dic
        for key,value in self.dic.items():
            self.dic[key] = np.mean(value)
            


if __name__=="__main__":
    list_of_sensor = []
    print("c'est parti")
    temperature = Sensor(123,"degre","Escalquens")
    pression_sensor = Sensor(34,"pression","Toulouse")
    humidite_sensor = Sensor(56,"humidite","Beziers")

    list_of_sensor.append(temperature)
    list_of_sensor.append(pression_sensor)
    list_of_sensor.append(humidite_sensor)

    agregateur1 = Agregator_moyenne(list_of_sensor)
    