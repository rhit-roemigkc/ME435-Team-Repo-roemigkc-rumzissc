import mqtt_helper as mh
import signal
import time
import gpiozero as gz

class App:
    def __init__(self):
        # DONE: set up pushbutton 
        
        
        # DONE: set up leds
        self.red_led = gz.LED(14)
        self.yellow_led = gz.LED(15)
        self.green_led = gz.LED(18)
        
        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/rumzissc/#",
                                 publish_topic_name="me435/rumzissc/to_computer")
        self.mqtt_client.callback = self.mqtt_callback

        self.top_button = gz.Button(23)
        self.top_button.when_pressed = lambda : self.mqtt_client.send_message("button")
        self.bot_button = gz.Button(25)
        self.bot_button.when_pressed = lambda : self.mqtt_client.send_message("reset")

    def mqtt_callback(self, message_type, message_payload):
        print("Recieved type:", message_type)
        print("Recieved payload:", message_payload)

        if message_type == "red":
            if message_payload == "on":
                self.red_led.on()
            elif message_payload == "off":
                self.red_led.off()

        if message_type == "yellow":
                if message_payload == 1:
                    self.yellow_led.on()
                elif message_payload == 0:
                    self.yellow_led.off()

        if message_type == "green":
            if message_payload:
                self.green_led.on()
            elif not message_payload:
                self.green_led.off()

        if message_type == "leds":
            if message_payload[0] == 1:
                self.red_led.on()
            else:
                self.red_led.off()
            if message_payload[1] == 1:
                self.yellow_led.on()
            else:
                self.yellow_led.off()
            if message_payload[2] == 1:
                self.green_led.on()
            else:
                self.green_led.off()


def main():
    print("GPIO MQTT")
    app = App()

    #  while True:
    #     #app.mqtt_client.send_message("red","on")
    #     #app.mqtt_client.send_message("yellow",1)
    #     #app.mqtt_client.send_message("green",True)
    #     app.mqtt_client.send_message("leds", [1, 0, 1])
    #     time.sleep(1)
    #     #app.mqtt_client.send_message("red","off")
    #     #app.mqtt_client.send_message("yellow",0)
    #     #app.mqtt_client.send_message("green",False)
    #     app.mqtt_client.send_message("leds", [0, 1, 0])
    #     time.sleep(1) 

    signal.pause() # keeps program running

main()