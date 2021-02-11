#!/usr/bin/python
# -*- coding: latin-1 -*-
import paho.mqtt.client as mqtt
import numpy as np
import time
import json

class AbstractAgregator:
    def __init__(self, name, city, latitude, longitude, time_to_wait):
        self.name = name
        self.city = city
        self.longitude = longitude
        self.latitude = latitude
        self.dic = {}
        self.temp_ext_buffer = []
        self.hum_buffer = []
        self.anemo_buffer = []
        self.indice_uv_buffer = []
        self.json_message = {
            "temp_ext": "",
            "hum": "",
            "anemo": "",
            "indice_uv": ""
        }
        self.local_message_received = {
            "temp_ext_sensor": False,
            "anemo_sensor": False,
            "hum_sensor": False,
            "indice_uv_sensor": False
        }
        self.time_to_wait = time_to_wait #sending json to the online broker each [time_to_wait] seconds

        
    def run_agregator(self):
        # MQTT Client 
        client = mqtt.Client(client_id="publisher-1") 
        client.connect("54.38.32.137",1883) 
        # Client mqtt local, récupération des sensors
        client_local = mqtt.Client(client_id="sensor_receiver")
        client_local.connect("localhost")
        client_local.on_message = self.on_message_local_client
        client_local.subscribe("/" + str(self.city) + "/temp_ext_sensor")
        client_local.subscribe("/" + str(self.city) + "/hum_sensor")
        client_local.subscribe("/" + str(self.city) + "/anemo_sensor")
        client_local.subscribe("/" + str(self.city) + "/indice_uv_sensor")
        
        #Starting client loop
        client_local.loop_start()
        client.loop_start()

        time_stamp = time.time()
        #Publish the mean value for each sensor to the online mqtt broker
        while(True):
            time_stamp_now = time.time()
            time.sleep(0.1)
            if(self.local_message_received.get("temp_ext_sensor")):
                client.publish("/data_plouf/" + str(self.name) + "/temp_ext", self.json_message.get("temp_ext"))
                self.local_message_received["temp_ext_sensor"] = False
            
            if(self.local_message_received.get("hum_sensor")):
                client.publish("/data_plouf/" + str(self.name) + "/hum", self.json_message.get("hum"))
                self.local_message_received["hum_sensor"] = False
            
            if(self.local_message_received.get("anemo_sensor")):
                client.publish("/data_plouf/" + str(self.name) + "/anemo", self.json_message.get("anemo"))
                self.local_message_received["anemo_sensor"] = False
            
            if(self.local_message_received.get("indice_uv_sensor")):
                client.publish("/data_plouf/" + str(self.name) + "/indice_uv", self.json_message.get("indice_uv"))
                self.local_message_received["indice_uv_sensor"] = False
            
            #Sending GPS each 10 seconds
            if(time_stamp_now - time_stamp > self.time_to_wait):
                client.publish("/data_plouf/" + str(self.name) + "/gps", str(self.latitude) + " " + str(self.longitude))
                time_stamp = time.time()


    #Add each local sensor value to his buffer or trigger the local_message_received if the buffer is full
    def on_message_local_client(self, client, userdata, message):
        ##### TEMP EXT SENSOR #####
        if message.topic == "/" + str(self.city) + "/temp_ext_sensor" :
            self.temp_ext_buffer.append(float(message.payload))
            if len(self.temp_ext_buffer) == self.time_to_wait : 
                self.dic["id"] = "temp_ext"
                self.dic["type"] = "degree"
                self.dic["value"] = np.mean(self.temp_ext_buffer)
                self.json_message["temp_ext"] = json.dumps(self.dic)
                self.temp_ext_buffer.clear()
                self.local_message_received["temp_ext_sensor"] = True
                return
            return

        ##### HUM SENSOR #####
        if message.topic == "/" + str(self.city) + "/hum_sensor" :
            self.hum_buffer.append(float(message.payload))
            if len(self.hum_buffer) == self.time_to_wait :
                self.dic["id"] = "hum"
                self.dic["type"] = "percentage"
                self.dic["value"] = np.mean(self.hum_buffer)
                self.json_message["hum"] = json.dumps(self.dic)
                self.hum_buffer.clear()
                self.local_message_received["hum_sensor"] = True
                return
            return

        ##### ANEMO SENSOR #####
        if message.topic == "/" + str(self.city) + "/anemo_sensor" :
            self.anemo_buffer.append(float(message.payload))
            if len(self.anemo_buffer) == self.time_to_wait : 
                self.dic["id"] = "anemo"
                self.dic["type"] = "km/h"
                self.dic["value"] = np.mean(self.anemo_buffer)
                self.json_message["anemo"] = json.dumps(self.dic)
                self.anemo_buffer.clear()
                self.local_message_received["anemo_sensor"] = True
                return
            return

        ##### INDICE UV SENSOR #####
        if message.topic == "/" + str(self.city) + "/indice_uv_sensor" :
            self.indice_uv_buffer.append(float(message.payload))
            if len(self.indice_uv_buffer) == self.time_to_wait :
                self.dic["id"] = "indice_uv"
                self.dic["type"] = "0-16"
                self.dic["value"] = np.mean(self.indice_uv_buffer)
                self.json_message["indice_uv"] = json.dumps(self.dic)
                self.indice_uv_buffer.clear()
                self.local_message_received["indice_uv_sensor"] = True
                return
            return
        


class Agregator_moyenne(AbstractAgregator):
    def __init__(self, name, city, latitude, longitude, time_to_wait):
        AbstractAgregator.__init__(self,  name, city, latitude, longitude, time_to_wait)
        self.run_agregator()
        
    #
    def computation(self):
        for key,value in self.dic.items():
            if key == "value":
                self.dic[key] = np.mean(value)
            


if __name__=="__main__":
    print("Starting agregator")
    agregateur1 = Agregator_moyenne("toulouse_agregator", "toulouse", 43.604734392639955, 1.4435127815107553, 2)