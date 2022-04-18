from sense_emu import SenseHat
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected OK')
    else:
        print(f'Bad connection. Returned code={rc}')


def connect_broker():
    broker = '10.0.2.2'
    client = mqtt.Client('Individual')
    print('Connecting to broker:', broker)
    client.connect(broker)
    client.loop_forever()


def start_sensehat():
    sense = SenseHat()
    stored_temperature = round(sense.get_temperature(), 0)

    while True:
        temperature = round(sense.get_temperature(), 0)
        if temperature != stored_temperature:
            stored_temperature = temperature
            if temperature > 34:
                print('hot')
            elif 34 > temperature > 24:
                print('medium')
            else:
                print('cold')


if __name__ == "__main__":
    connect_broker()
    start_sensehat()
