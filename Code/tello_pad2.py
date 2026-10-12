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


""" class pad:
    id
    x
    y
    z

    def __init__(self, id, x, y, z):
        self.id = id  # Instance attribute
        self.x = x
        self.y = y
        self.z = z
         
         """     
         
def search_for_pad_spiral(currentID,spiral_mult=1):
    if(spiral_mult >= 50):
        return -1
    tello.move_forward(20*spiral_mult)
    if(currentID == tello.get_mission_pad_id()):
        tello.rotate_clockwise(90)
        return search_for_pad_spiral(current_id, spiral_mult + 1)

    return detected_id


def move_to_pad(target_id):
    x = tello.get_mission_pad_distance_x()
    y = tello.get_mission_pad_distance_y()
    z = tello.get_mission_pad_distance_z()
    tello.go_xyz_speed_mid(x, y, z, 20, target_id)
    tello.land()


desired_pad_count = 2
pad_ids = []

# Start on current pad.
tello.takeoff()
tello.move_up(40)

current_id = tello.get_mission_pad_id()
pad_ids.append(current_id)

while len(pad_ids) < desired_pad_count:
    new_pad_id = search_for_pad_spiral(current_id)
    batteryValue = tello.get_battery()
    print(f"Battery value: {batteryValue}%")

    if new_pad_id not in pad_ids:
        current_id = new_pad_id
        move_to_pad(new_pad_id)
        tello.takeoff()
        pad_ids.append(new_pad_id)

print("Reached desired mission pad count.")
tello.end()
        

