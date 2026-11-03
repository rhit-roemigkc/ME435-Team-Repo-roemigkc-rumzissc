import motor
import time

class DriveSystem:
    def __init__(self):
        self.car = motor.OrdinaryCar()

    def scale_speed(self, speed):
        """ Returns an int duty of 0 to 4095 (or to -4095) based on the given speed """
        return int(speed / 100 * 4095)

    def set_speeds(self, left_front, left_rear, right_front, right_rear):
        """ Pass in 4 speeds each -100 to 100 to set wheel duty cycle """
        self.car.set_motor_model(self.scale_speed(left_front),
                                 self.scale_speed(left_rear),
                                 self.scale_speed(right_front),
                                 self.scale_speed(right_rear))


    def go(self, left_wheel_speed, right_wheel_speed):
        """ Speeds as integers from -100 to 100. """
        left_wheel_speed = self.scale_speed(left_wheel_speed)
        right_wheel_speed = self.scale_speed(right_wheel_speed)
        self.set_speeds(left_wheel_speed, left_wheel_speed, right_wheel_speed, right_wheel_speed)

    def stop(self):
        self.set_speeds(0,0,0,0)

    def go_straight_for_seconds(self, seconds, speed):
        speed = self.scale_speed(speed)
        self.go(speed, speed)
        time.sleep(seconds)
        self.stop()

    def go_straight_for_inches(self, inches, speed):
        m = 0.2
        B  = 0
        inches_per_second = m * speed + B
        seconds = inches/inches_per_second
        self.go_straight_for_seconds(seconds, speed)

    def spin_in_place_for_seconds(self, seconds, speed):
        """ +speed -> cw ... -speed -> ccw"""
        speedAdj = self.scale_speed(speed)
        self.set_speeds(-speedAdj,0,0,speedAdj)
        time.sleep(seconds)
        self.stop()

    def spin_in_place_for_degrees(self, degrees, speed):

        if degrees > 180:
            degrees = abs(degrees-360)
            speed = - speed

        speedAdj = self.scale_speed(speed)
        m = 0.25
        B = 0
        deg_per_sec = m * speedAdj + B

        seconds = degrees/deg_per_sec
        self.spin_in_place_for_seconds(seconds, speedAdj)

    def draw_polygon(self, speed, sides, inches):
        degrees = 360/sides

        for i in range(sides):
            self.go_straight_for_inches(inches, speed)
            time.sleep(0.5)
            self.spin_in_place_for_degrees(degrees, speed)
            time.sleep(0.5)