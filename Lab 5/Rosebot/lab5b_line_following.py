from rosebot import Rosebot
import time

def main():
    print("Lab 5b Line Following")
    robot = Rosebot()
    speed = int(13)

    try:
        while True:

            if robot.ultrasonic.get_cm() < 20:
                robot.drive_system.stop()
            else:
                word = robot.line_sensors.get_line_word()
                if word == "BBB":
                    robot.drive_system.set_speeds(speed, speed, speed, speed)
                elif word == "BBW":
                    robot.drive_system.set_speeds(-speed, -speed, speed, speed)
                elif word == "BWB":
                    robot.drive_system.stop()
                elif word == "BWW":
                    robot.drive_system.set_speeds(-speed, -speed, speed, speed)
                elif word == "WBB":
                    robot.drive_system.set_speeds(speed, speed, -speed, -speed)
                elif word == "WBW":
                    robot.drive_system.set_speeds(speed, speed, speed, speed)
                elif word == "WWB":
                    robot.drive_system.set_speeds(speed, speed, -speed, -speed)
                elif word == "WWW":
                    robot.drive_system.stop()
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        # handle control C exit
        robot.drive_system.stop()
        print("\nGoodbye!")

main()