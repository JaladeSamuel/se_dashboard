import paho.mqtt.client as mqtt


# Creating client
client = mqtt.Client(client_id='publisher-1')

# Connect to broker
client.connect("54.38.32.137",1883)

# Publish a message with topic
ret= client.publish("data_plouf/sensor_meteo","message de test helloooo")

# Run a loop
client.loop()