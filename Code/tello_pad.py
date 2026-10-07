from djitellopy import Tello

tello = Tello()

tello.connect()

batteryValue = tello.get_battery()
print(f"Battery value: {batteryValue}%")

if(batteryValue < 20):
    print("Battery too low for flight. Please charge the battery.")
    tello.end()
    exit()

tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2)

tello.takeoff()

counter = 0

while counter < 10:
    pad = tello.get_mission_pad_id()
    print(pad)

    if pad == 2:
        x = tello.get_mission_pad_distance_x()
        y = tello.get_mission_pad_distance_y()
        z = tello.get_mission_pad_distance_z()

        tello.go_xyz_speed_mid(x, y, z, 20, pad)

        tello.land()
        tello.end()
        break
    else :
        tello.move_forward(20)
        counter += 1
