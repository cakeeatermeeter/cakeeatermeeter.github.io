from djitellopy import Tello

tello = Tello()

def getBatteryValue():
    batteryValue = tello.get_battery()
    print(f"Battery value: {batteryValue}%")
    batteryCheck(batteryValue)

def batteryCheck(batteryValue):
    if(batteryValue < 20):
        print("Battery too low for flight. Please charge the battery.")
        tello.end()
        exit()
