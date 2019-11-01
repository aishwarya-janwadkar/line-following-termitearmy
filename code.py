import time
from adafruit_crickit import crickit

crickit.drive_1.frequency = 1000

def moveForward():

    crickit.continuous_servo_1.throttle = 1 #left
    crickit.continuous_servo_2.throttle = -1 #right

def turnRight():

    crickit.continuous_servo_1.throttle = 0.5
    crickit.continuous_servo_2.throttle = -0.05

def turnLeft():

    crickit.continuous_servo_1.throttle = -0.05
    crickit.continuous_servo_2.throttle = -0.75

def stop():

    crickit.continuous_servo_1.throttle = -0.05
    crickit.continuous_servo_2.throttle = -0.05

def drum():

    for i in range(0,20):
        crickit.drive_1.fraction = 1.0  # all the way on
        time.sleep(0.005)
        crickit.drive_1.fraction = 0.0  # all the way off

ss = crickit.seesaw
# sensor1 connected to signal #1
sensor1 = crickit.SIGNAL1
sensor2 = crickit.SIGNAL8

while True:

    print((ss.analog_read(sensor1),))
    print((ss.analog_read(sensor2),))

    if ss.analog_read(sensor1) < 15 and ss.analog_read(sensor2) < 15:
        moveForward()
        print("forward")

    elif ss.analog_read(sensor1) > 15 and ss.analog_read(sensor2) <= 15:
        turnRight()
        print("Right")

    elif ss.analog_read(sensor2) > 15 and ss.analog_read(sensor1) <= 15:
        turnLeft()
        print("Left")

    else:
        stop()
        drum()
        print("stop")

    time.sleep(.5)