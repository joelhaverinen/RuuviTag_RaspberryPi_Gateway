import time
from ruuvitag_sensor.ruuvitag import RuuviTag
from timeout_decorator import timeout # pip install timeout-decorator


sensor = RuuviTag("EC:28:C9:6E:9F:51")

timeout_seconds = 1  # Aseta haluamasi timeout-aika sekunteina

@timeout(timeout_seconds)
def update_sensor():
    return sensor.update()

try:
    state = update_sensor()
except TimeoutError:
    print('Timeout occurred while updating sensor.')

    
# get latest state (does not get it from the device)
state = sensor.state

# Check if the MAC address is the expected one
expected_mac_address = "ec28c96e9f51"

data = state


if state and 'mac' in state and state['mac'] == expected_mac_address: # täs muodos ec28c96e9f51 ei täs EC:28:C9:6E:9F:51
    # If the MAC address is found, continue with the current logic
    #data = state
    temperature = data['temperature']
    mac_address = data['mac']
else:
    # If the MAC address is not found, set default values
    data = {'temperature': 'N/A', 'mac': 'N/A'}
    temperature = data['temperature']
    mac_address = data['mac']



print("Temperature:", temperature)
print("MAC Address:", mac_address)
