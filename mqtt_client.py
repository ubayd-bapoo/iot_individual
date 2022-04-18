from sense_emu import SenseHat
import paho.mqtt.client as mqtt

broker = '10.0.2.2'

client = mqtt.Client('test1')
print('Connecting to broker:', broker)
client.connect(broker)
client.disconnect()

sense = SenseHat()
stored_temperature = sense.get_temperature()

while True:
    temperature = sense.get_temperature()
    if temperature != stored_temperature:
        print(temperature, stored_temperature)
        stored_temperature = temperature
    #     if temperature > 34:
    #         print('hot')
    #     elif 34 > temperature > 24:
    #         print('medium')
    #     else:
    #         print('cold')
