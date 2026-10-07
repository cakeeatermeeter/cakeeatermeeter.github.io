from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_forward(50)
tello.rotate_clockwise(120)
tello.move_forward(100)
tello.rotate_counter_clockwise(120)
tello.move_forward(50)
tello.rotate_counter_clockwise(120)
tello.move_forward(100)
tello.rotate_clockwise(120)

tello.land()
tello.end()