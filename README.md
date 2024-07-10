# mrt-api for sensor readings

## todo:

- SoC calculations (done)
- RPM calculations (done)
- Distance travelled logic (done)
- Send an email
- Documentation
- Testing
- Server fork (possibly)
- Add data-acquisition to requirements.txt or requirements2.txt

## setup:

### Create virtual environment

- `sudo apt install python3.8-venv`
- `python3 -m venv venv`
- `source venv/bin/activate`

### Install dependencies

- `pip install -r requirements.txt`

### Run server

- `python3 app.y`

### Use client.py for testing (preferably outside of virtual environment)

- `python3 client.py`


### Endpoints

- `/voltage_current_soc`
  data: voltage, current, soc
- `/speed`
  data: speed, rpm, distance
- `/blinkers_temperature`
  data: blinkers, temperature
- `/gps`
  data: gps_lat, gps_long