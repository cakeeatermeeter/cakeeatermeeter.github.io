from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_forward(50)
tello.rotate_counter_clockwise(90)
tello.move_forward(50)
tello.land()