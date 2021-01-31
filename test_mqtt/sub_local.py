import paho.mqtt.client as mqtt #import the client

# Function to process recieved message
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))


# Create client
client = mqtt.Client(client_id="subscriber-1")

# Assign callback function
client.on_message = on_message

# Connect to broker
client.connect("localhost")

# Subscriber to topic
client.subscribe("/toulouse/temp_ext_sensor") # nom du capteur

# Run loop
client.loop_forever()