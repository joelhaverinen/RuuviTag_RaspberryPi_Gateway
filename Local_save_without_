import csv
from datetime import datetime
import time
from ruuvitag_sensor.ruuvitag import RuuviTag
from timeout_decorator import timeout

def mittaus_tallennus():
    # Hae nykyinen aika ja päivämäärä
    nyt = datetime.now()
    aika_pvm = nyt.strftime("%Y-%m-%d_%H-%M-%S")  

    #Sensor:
    sensor = RuuviTag("EA:D0:02:27:0D:F6")

    
    state = sensor.update()
    #state = update_sensor()
    

    # get latest state (does not get it from the device)
    state = sensor.state

    # Check if the MAC address is the expected one (ec28c96e9f51) 
    expected_mac_address = "ead002270df6"

    data = state


    if state and 'mac' in state and state['mac'] == expected_mac_address: 
        # If the MAC address and state is found, continue with the current logic
      
        temperature = data['temperature']
        mac_address = data['mac']
        battery = data['battery']
        humidity = data['humidity']
        pressure = data['pressure']
        tx_power = data['tx_power']
        
        battery = battery /1000
        time.sleep(2)       # Odota 
    else:
        # If the MAC address and state is not found, set default values
        data = {'battery': 'N/A','pressure': 'N/A', 'temperature': 'N/A', 'humidity': 'N/A', 'tx_power': 'N/A', 'mac': 'N/A'}
        temperature = data['temperature']
        mac_address = data['mac']
        battery = data['battery']
        humidity = data['humidity']
        pressure = data['pressure']
        tx_power = data['tx_power']
        
    print("Temperature:", temperature)
    print("Battery:", battery)
    #print("MAC Address:", mac_address)

    # Luo CSV-tiedoston ja kyseinen aika tiedoston nimeksi
    tiedoston_nimi = f"{aika_pvm}.csv"
    with open(tiedoston_nimi, mode='w', newline='') as tiedosto:
        csv_tiedosto = csv.writer(tiedosto)

        # Tiedot CSV-tiedostoon
        #csv_tiedosto.writerow(['Time','Temperature','MAC']) # ehkä parempi ilman otsikoita
        csv_tiedosto.writerow([aika_pvm, battery, pressure, temperature, humidity, tx_power, mac_address])
        

    print(f"Luotu CSV-tiedosto: {tiedoston_nimi}")

if __name__ == "__main__":
    while True:
        mittaus_tallennus()
        
