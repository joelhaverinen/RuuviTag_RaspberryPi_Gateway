# RuuviTag_RaspberryPi_Gateway
RuuviTag BLE sensor sending data to RaspberryPi



Install the latest development version from https://github.com/ttu/ruuvitag-sensor

$ python -m venv .venv

$ source .venv/bin/activate

$ python -m pip install git+https://github.com/ttu/ruuvitag-sensor


Try to find all tags:

$ python3 -m ruuvitag_sensor -f
