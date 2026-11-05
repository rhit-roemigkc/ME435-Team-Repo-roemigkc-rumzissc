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
            # get ultrasonic sensor

            # if distance < 20 cm, stop robot
            if robot.ultrasonic.get_cm() < 20:
                robot.drive_system.stop()
            else:
                # get the line sensor readings
                word = robot.line_sensors.get_line_word()
                left = word[0]
                middle = word[1]
                right = word[2]

                if middle == 'B':
                    front_left_speed = 20
                    rear_left_speed = 20
                    front_right_speed = 20
                    rear_right_speed = 20

                if left == 'B': 
                    front_left_speed = 20
                    rear_left_speed = 20
                    front_right_speed = 30
                    rear_right_speed = 30

                if right == 'B':
                    front_left_speed = 30
                    rear_left_speed = 30
                    front_right_speed = 20
                    rear_right_speed = 20

                robot.drive_system.set_speeds(front_left_speed, rear_left_speed, front_right_speed, rear_right_speed)

                # if middle == 'B':
                #     robot.drive_system.set_speeds(20, 20, 20, 20)
                # elif left == 'B':
                #     robot.drive_system.set_speeds(20, 20, 35, 35)
                # elif right == 'B':
                #     robot.drive_system.set_speeds(35, 35, 20, 20)
                

            time.sleep(0.1)

    except KeyboardInterrupt:
        # handle control C exit
        robot.drive_system.stop()
        print("Goodbye!")

main()