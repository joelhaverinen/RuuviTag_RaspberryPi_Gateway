import csv
from datetime import datetime
import time
from ruuvitag_sensor.ruuvitag import RuuviTag

def luo_csv_tiedosto():
    # Hae nykyinen aika ja päivämäärä
    nyt = datetime.now()
    aika_pvm = nyt.strftime("%Y-%m-%d_%H-%M-%S")  # Muotoile aika ja päivämäärä

    sensor = RuuviTag("EC:28:C9:6E:9F:51")
    # update state from the device
    state = sensor.update()

    # get latest state (does not get it from the device)
    state = sensor.state

 

    data = state
    temperature = data['temperature']
    mac_address = data['mac']

    #print("Temperature:", temperature)
    #print("MAC Address:", mac_address)

    # Luo CSV-tiedosto nimen perusteella
    tiedoston_nimi = f"{aika_pvm}.csv"
    with open(tiedoston_nimi, mode='w', newline='') as tiedosto:
        csv_tiedosto = csv.writer(tiedosto)

        # Kirjoita esimerkiksi joitakin tietoja CSV-tiedostoon
        csv_tiedosto.writerow(['Time', 'MAC', 'Temperature'])
        csv_tiedosto.writerow([aika_pvm, mac_address, temperature])
        

    print(f"Luotu CSV-tiedosto: {tiedoston_nimi}")

if __name__ == "__main__":
    while True:
        luo_csv_tiedosto()
        time.sleep(5)       # Odota 5 sek.

