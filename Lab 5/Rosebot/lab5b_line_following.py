from rosebot import Rosebot
import time
def main():
    print("Lab 5b Line Following")
    robot = Rosebot()

    try:
        while True:
            # get ultrasonic sensor

            # if distance < 20 cm, stop robot

            # else

            # get the line sensor readings
            # adjust wheel speeds based on our strategy



            time.sleep(0.1)

    except KeyboardInterrupt:
        # handle control C exit
        robot.drive_system.stop()
        print("Goodbye!")

main()