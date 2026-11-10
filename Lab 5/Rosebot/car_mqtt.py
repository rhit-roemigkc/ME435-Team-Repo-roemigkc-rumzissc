import mqtt_helper as mh
from rosebot import Rosebot
import datetime
import time

class App:
    def __init__(self):
        self.robot = Rosebot()
        self.is_streaming = False
        self.mode = "none"

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/rumzissc/to_pi",
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

        if message_type == "is_streaming":
            self.is_streaming = message_payload

        if message_type == "mode":
            self.mode = message_payload
            if self.mode == "none":
                self.robot.drive_system.stop()


def main():
    print("GPIO MQTT")
    app = App()
    last_time_sent_s = 0

    try:
        while True:
            right_now = datetime.datetime.now()
            current_time_s = right_now.timestamp()

            if app.is_streaming and current_time_s > last_time_sent_s + 2.0:
                last_time_sent_s = current_time_s
                app.mqtt_client.send_message("line_sensor_reading",{
                    "timestamp": right_now.strftime("%m,%d,%Y  %H:%M:%S"),
                    "left": app.robot.line_sensors.get_left(),
                    "middle": app.robot.line_sensors.get_middle(),
                    "right": app.robot.line_sensors.get_right()
                })

            if app.mode == "drive_until_wall":
                if app.robot.ultrasonic.get_cm() < 30:
                    app.robot.drive_system.stop()
                    app.robot.buzzer.beep(on_time=0.1, off_time=0.1, n=3)
                    app.mode = "none"
                else:
                    app.robot.drive_system.go(20, 20)

            if app.mode == "drive_until_line":
                if app.robot.line_sensors.get_line_word != "WWW":
                    app.robot.drive_system.stop()
                    app.robot.buzzer.beep(on_time=0.1, off_time=0.1, n=3)
                    app.mode = "none"
                else:
                    app.robot.drive_system.go(20, 20)

            if app.mode == "line_follow":
                if app.robot.ultrasonic.get_cm() < 20:
                    app.robot.drive_system.stop()
                else:
                    word = app.robot.line_sensors.get_line_word()
                    speed = int(13)
                    if word == "BBB":
                        app.robot.drive_system.set_speeds(speed, speed, speed, speed)
                    elif word == "BBW":
                        app.robot.drive_system.set_speeds(-speed, -speed, speed, speed)
                    elif word == "BWB":
                        app.robot.drive_system.stop()
                        app.mode = "none"
                    elif word == "BWW":
                        app.robot.drive_system.set_speeds(-speed, -speed, speed, speed)
                    elif word == "WBB":
                        app.robot.drive_system.set_speeds(speed, speed, -speed, -speed)
                    elif word == "WBW":
                        app.robot.drive_system.set_speeds(speed, speed, speed, speed)
                    elif word == "WWB":
                        app.robot.drive_system.set_speeds(speed, speed, -speed, -speed)
                    elif word == "WWW":
                        app.robot.drive_system.stop()
                        app.mode = "none"
                            
                    time.sleep(0.1)

    except KeyboardInterrupt:
        print("Goodbye")
        app.robot.drive_system.stop
        app.mqtt_client.close()

main()