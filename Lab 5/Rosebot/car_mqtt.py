import mqtt_helper as mh
from rosebot import Rosebot
import signal
import time

class App:
    def __init__(self):
        self.robot = Rosebot()

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/rumzissc/#",
                                 publish_topic_name="me435/rumzissc/to_computer")
        self.mqtt_client.callback = self.mqtt_callback

    def mqtt_callback(self, message_type, message_payload):
        print("Recieved type:", message_type)
        print("Recieved payload:", message_payload)

        if message_type == "set_speeds":
            self.robot.drive_system.set_speeds(message_payload[0],message_payload[1],message_payload[2],message_payload[3])
        if message_type == "stop":
            self.robot.drive_system.stop()
        
        if message_type == "beep":
            self.robot.buzzer.beep(on_time=0.1, off_time=0.3, n=2)



def main():
    print("GPIO MQTT")
    app = App()

    try:
        # while True:
        #     app.mqtt_client.send_message("beep")
        #     time.sleep(2)

        signal.pause() # keeps program running

    except KeyboardInterrupt:
        print("Goodbye")
        app.robot.drive_system.stop
        app.mqtt_client.close()

main()