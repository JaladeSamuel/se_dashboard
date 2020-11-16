import paho.mqtt.client as paho
import random
import time

broker ="54.38.32.137"
port = 1883

def read_temp():
    time.sleep(1)
    return random.randint(0,30)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


client = paho.Client("rasp_sender")                           
#client.username_pw_set("upssitech","2011")
client.on_connect = on_connect
client.connect(broker,port)                              

client.loop_start()

while True:
    temperature = read_temp() #doit être bloquant
    print(temperature)
    client.publish("rasp/sensors/temperature", str(temperature))

