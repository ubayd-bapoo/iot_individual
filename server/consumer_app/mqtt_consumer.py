import json
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print('Subscribe to MQTT topic')
    client.subscribe("topic/test")


def on_message(client, userdata, msg):
    from .constants import SENSEHAT_SOURCE, SENSEHAT_SENSORS
    from .models import SensehatReading
    message = json.loads(msg.payload.decode("utf-8"))
    print(f"Reading MQTT data: {message}")

    try:
        print("Saving MQTT to DB")
        SensehatReading.objects.create(sensehat_sensor=0, source=0, reading=message['temp'])
    except:
        print("Error Saving MQTT to DB")
        pass


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost")
