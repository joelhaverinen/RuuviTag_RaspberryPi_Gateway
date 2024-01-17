import os
import re
import time
import csv
import json
import requests
from ruuvitag_sensor.ruuvitag import RuuviTag
import threading

# IoThook API details
iothook_url = 'http://iothook.com/api/update/'
api_key = 'xxxxxxxxxxxxxxxxxxxx'  # Replace with your IoThook API key data
api_key2 = 'xxxxxxxxxxxxxxxxxxxx'  # Replace with your IoThook API key Uplink

# Function to initialize the RuuviTag sensor
def initialize_sensor():
    try:
        sensor = RuuviTag('EC:28:C9:6E:9F:51')
        return sensor
    except Exception as e:
        print(f"Error initializing sensor: {e}")
        return None

# Function to find the next available CSV file number
def find_next_csv_number():
    measurement_files = [f for f in os.listdir() if re.match(r'Measurement_\d+\.csv', f)]
    if not measurement_files:
        return 1  # If no files exist, start from 1

    numbers = [int(re.search(r'\d+', f).group()) for f in measurement_files]
    return max(numbers) + 1

# Function to update the sensor data in a separate thread
def update_sensor_data(sensor, data_holder):
    try:
        data_holder['state'] = sensor.update()
    except Exception as e:
        print(f"Error updating sensor data: {e}")

# Function to handle main logic
def main_logic():
    csv_number = find_next_csv_number()
    last_data_time = time.time()

    while True:
        try:
            # Your existing code here

            # Create a dictionary to hold the sensor state
            data_holder = {'state': None}

            # Create a thread to update sensor data
            sensor_thread = threading.Thread(target=update_sensor_data, args=(sensor, data_holder))
            sensor_thread.start()

            # Wait for the sensor update thread to finish or until a timeout
            sensor_thread.join(timeout=10)  # Timeout set to 10 seconds

            # Check if the update is successful
            state = data_holder['state']
            if not state:
                print("No data received from RuuviTag within the timeout. Sending uplink_test message.")
                send_to_iothook(api_key2, {"field_1": "1"})
                last_data_time = time.time()
                continue  # Skip the rest of the loop and restart

            
            try:
                # Print and write to CSV
                data = {
                    'field_1': "{:.3f}".format(state["temperature"]),
                    'field_2': "{:.3f}".format(state["battery"] / 1000),
                    'field_3': str(state["pressure"]),
                    'field_4': "{:.3f}".format(state["humidity"]),                    
                }
                for key, value in data.items():
                    print(f'{key}: {value}')

                # Send data to IoThook
                send_to_iothook(api_key, data)
                send_to_iothook(api_key2, {"field_1": "2"})

            except Exception as e:
                print(f"An error occurred while processing sensor data: {e}")

            last_data_time = time.time()
            csv_number += 1

        except Exception as e:
            print(f"An error occurred: {e}")

            # Retry or restart logic
            print("Retrying in 10 seconds...")
            time.sleep(10)
            continue

        # Check for a timeout (no data received in 2 minutes) uplink
        if time.time() - last_data_time > 120:
            print("No data received in 2 minutes. Sending uplink_test message.")
            send_to_iothook(api_key2, {"field_1": "1"})
            last_data_time = time.time()

# Function to send data to IoThook
def send_to_iothook(api_key, data):
    headers = {'Content-type': 'application/json'}
    data['api_key'] = api_key
    response = requests.post(iothook_url, data=json.dumps(data), headers=headers)
    print("IoThook response:", response.text)

# Main program
while True:
    sensor = initialize_sensor()
    if sensor:
        main_logic()
        
