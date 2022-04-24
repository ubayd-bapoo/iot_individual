import json
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print('Subscribe to MQTT topic')
    client.subscribe("topic/test")


def on_message(client, userdata, msg):
    print("message received ", str(msg.payload.decode("utf-8")))
    print("message testing ", json.loads(msg.payload.decode("utf-8"))['temp'])
    print("message topic=", msg.topic)
    print("message qos=", msg.qos)
    print("message retain flag=", msg.retain)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost")
