from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_forward(25)
tello.rotate_counter_clockwise(45)
tello.move_forward(25)
tello.rotate_clockwise(45)
tello.move_forward(25)
tello.rotate_counter_clockwise(45)
tello.move_forward(25)
tello.rotate_clockwise(45)
tello.move_forward(25)

tello.land()