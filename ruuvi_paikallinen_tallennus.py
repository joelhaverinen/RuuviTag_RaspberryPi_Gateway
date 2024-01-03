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
    sensor = RuuviTag("EC:28:C9:6E:9F:51")

    #Timeout
    timeout_seconds = 1

    # update state from the device and timeout
    @timeout(timeout_seconds)
    def update_sensor():
        return sensor.update()

    try:
        state = update_sensor()
    except TimeoutError:
        print('Timeout occurred while updating sensor.')
    

    # get latest state (does not get it from the device)
    tate = sensor.state

    # Check if the MAC address is the expected one
    expected_mac_address = "ec28c96e9f51"

    data = state


    if state and 'mac' in state and state['mac'] == expected_mac_address: # (ec28c96e9f51) 
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
    #print("MAC Address:", mac_address)

    # Luo CSV-tiedosto nimi ajan perusteella
    tiedoston_nimi = f"{aika_pvm}.csv"
    with open(tiedoston_nimi, mode='w', newline='') as tiedosto:
        csv_tiedosto = csv.writer(tiedosto)

        # Kirjoita esimerkiksi joitakin tietoja CSV-tiedostoon
        #csv_tiedosto.writerow(['Time','Temperature','MAC']) # ehkä parempi ilman otsikoita
        csv_tiedosto.writerow([aika_pvm, temperature, mac_address])
        

    print(f"Luotu CSV-tiedosto: {tiedoston_nimi}")

if __name__ == "__main__":
    while True:
        mittaus_tallennus()
        time.sleep(5)       # Odota 5 sek.

