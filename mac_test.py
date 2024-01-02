import time
from ruuvitag_sensor.ruuvitag import RuuviTag

sensor = RuuviTag("EC:28:C9:6E:9F:51")

state = sensor.update() # will freeze here if sensor not found

# print the current state
print("Current State:", state)

# get latest state (does not get it from the device)
state = sensor.state

# print the updated state
print("Updated State:", state)

# Check if the MAC address is the expected one
expected_mac_address = "ec28c96e9f51"


data = state

print(sensor)
print(mac_address)


if state and 'mac' in state and state['mac'] == expected_mac_address: # täs muodos ec28c96e9f51 ei täs EC:28:C9:6E:9F:51
    # If the MAC address is found, continue with the current logic
    #data = state
    temperature = data['temperature']
    mac_address = data['mac']
else:
    # If the MAC address is not found, set default values
    data = {'temperature': 'N/A', 'mac': 'Not Available'}
    temperature = data['temperature']
    mac_address = data['mac']



print("Temperature:", temperature)
print("MAC Address:", mac_address)
