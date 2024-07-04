from .config import socketio
from . import views
from .config import db
from .models import SensorReadings


@socketio.on('connect', namespace="/")
def handle_connect():
    print('Client connected')
    socketio.emit('message', 'Connected')


def update_voltage_range_current(data):
    voltage = float(data.get('voltage'))
    current = float(data.get('current'))
    range_available = data.get('range')
    soc = int(data.get(soc))
    socketio.emit('vi_range', {
        'voltage': voltage,
        'current': current,
        'range': range_available,
        'soc': soc
    })
    voltage_current_range_readings = SensorReadings(
        voltage=voltage, current=current, range_available=range_available, soc=soc)
    db.session.add(voltage_current_range_readings)
    db.session.commit()


def update_speed_rpm_distance(data):
    speed = int(data.get('speed'))
    rpm = int(data.get('rpm'))
    distance = int(data.get('distance'))
    socketio.emit('speed', {
        'speed': speed,
        'rpm': rpm,
        'distance': distance
    })
    speed_rpm_distance = SensorReadings(
        speed=speed, rpm=rpm, distance=distance)
    db.session.add(speed_rpm_distance)
    db.session.commit()


def update_blinkers_temperature(data):
    socketio.emit('blinkers', {
        'blinkers': int(data.get('blinkers')),
    })
    socketio.emit('battery_temperature', {
        'temperature': int(data.get('temperature')),
    })
    temp_readings = SensorReadings(temperature=temperature)
    db.session.add(temp_readings)
    db.session.commit(temp_readings)


def update_gps(data):
    gps_lat = data.get('gps_lat')
    gps_long = data.get('gps_long')
    gps_data = SensorReadings(gps_lat=gps_lat, gps_long=gps_long)
    db.session.add(gps_data)
    db.session.commit()
