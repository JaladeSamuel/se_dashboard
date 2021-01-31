import paho.mqtt.client as mqtt #import the client

# Function to process recieved message
def process_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))


# Create client
client = mqtt.Client(client_id="subscriber-1")

# Assign callback function
client.on_message = process_message

# Connect to broker
client.connect("54.38.32.137",1883,60)

# Subscriber to topic
client.subscribe("/data_plouf/toulouse_agregator/temp_cpu") # nom de l'agregateur

# Run loop
client.loop_forever()
