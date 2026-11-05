from rosebot import Rosebot
import time

def main():
    print("Lab 5b Line Following")
    robot = Rosebot()
    front_left_speed = 20
    rear_left_speed = 20
    front_right_speed = 20
    rear_right_speed = 20

    try:
        while True:

            print(robot.ultrasonic.get_cm())
            print(robot.line_sensors.get_line_word())

            if robot.ultrasonic.get_cm() < 20:
                robot.drive_system.stop()
            else:
                word = robot.line_sensors.get_line_word()
                if word == "BBB":
                    robot.drive_system.set_speeds(15, 15, 15, 15)
                elif word == "BBW":
                    robot.drive_system.set_speeds(-15, -15, 15, 15)
                elif word == "BWB":
                    robot.drive_system.stop()
                elif word == "BWW":
                    robot.drive_system.set_speeds(-15, -15, 15, 15)
                elif word == "WBB":
                    robot.drive_system.set_speeds(15, 15, -15, -15)
                elif word == "WBW":
                    robot.drive_system.set_speeds(15, 15, 15, 15)
                elif word == "WWB":
                    robot.drive_system.set_speeds(15, 15, -15, -15)
                elif word == "WWW":
                    robot.drive_system.stop()
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        # handle control C exit
        robot.drive_system.stop()
        print("Goodbye!")

main()