import paho.mqtt.client as mqtt #import the client

# Function to process recieved message
def process_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))


# Create client
client = mqtt.Client()

# Assign callback function
client.on_message = process_message

# Connect to broker
client.connect("54.38.32.137",1883)

# Subscriber to topic
client.subscribe("/data_plouf/toulouse_agregator/temp_ext")
client.subscribe("/data_plouf/toulouse_agregator/hum")
client.subscribe("/data_plouf/toulouse_agregator/anemo")
client.subscribe("/data_plouf/toulouse_agregator/indice_uv")
client.subscribe("/data_plouf/toulouse_agregator/gps")  

# Run loop
client.loop_forever()
