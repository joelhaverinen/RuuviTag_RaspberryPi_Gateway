# example from https://github.com/ttu/ruuvitag-sensor

from ruuvitag_sensor.ruuvitag import RuuviTag

sensor = RuuviTag("AA:2C:6A:1E:59:3D") # RuuviTag MAC address 

# update state from the device
state = sensor.update()

# get latest state (does not get it from the device)
state = sensor.state

print(state)
