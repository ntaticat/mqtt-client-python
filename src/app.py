import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

load_dotenv()

MQTT_CLIENT_URL = os.getenv('MQTT_CLIENT_URL')
MQTT_CLIENT_PORT = os.getenv('MQTT_CLIENT_PORT')
TOPIC = os.getenv('TOPIC')

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    msg.topic
    print(msg.payload)
    print(client)
    print(userdata) 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_CLIENT_URL, MQTT_CLIENT_PORT, 60)

client.loop_forever()
