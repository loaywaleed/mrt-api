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

- `POST /voltage_current_soc_temperature`
  data: voltage, current, soc
- `POST /speed_rpm_distance`
  data: speed, rpm, distance
- `POST /blinkers`
  data: blinkers
- `POST /gps`
  data: gps_lat, gps_long
- `POST /range`
  data: hours
- `POST /emergency`
  data: email_var