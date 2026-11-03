import mqtt_helper as mh
import signal
import time

class App:
    def __init__(self):
        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/rumzissc/#",
                                 publish_topic_name="me435/rumzissc/to_computer")
        self.mqtt_client.callback = self.mqtt_callback

    def mqtt_callback(self, message_type, message_payload):
        print("Recieved type:", message_type)
        print("Recieved payload:", message_payload)


def main():
    print("GPIO MQTT")
    app = App()

    while True:
        app.mqtt_client.send_message("set_speeds", [40, 40, 40, 40])
        time.sleep(1)
        app.mqtt_client.send_message("set_speeds", [0, 0, 0, 0])
        time.sleep(1) 

    # signal.pause() # keeps program running

main()