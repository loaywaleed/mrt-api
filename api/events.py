from .config import socketio
from . import views
#from .config import db
#from .models import SensorReadings


@socketio.on('connect', namespace="/")
def handle_connect():
    print('Client connected')
    socketio.emit('message', 'Connected')


def update_voltage_current_soc_temp(data):
    try:
        socketio.emit('vi', {
            'voltage': float(data.get('voltage')),
            'current': float(data.get('current')),
        })
        socketio.emit('soc', {
            'soc': int(data.get('soc')),
        })
        socketio.emit('battery_temperature', {
            'temperature': int(data.get('temp')),
        })
        # voltage_current_soc_readings = SensorReadings(
        #     voltage=voltage, current=current, soc=soc)
        # db.session.add(voltage_current_soc_readings)
        # db.session.commit()
    except:
        print("Failed to deserialize JSON data")


def update_range_available(data):
    hours_available = data.get('hours')
    average_speed = 30
    range_available = hours_available * average_speed
    socketio.emit('range', {
        'range': range_available,
    })
    # range_available_readings = SensorReadings(range_available=range_available)
    # db.session.add(range_available_readings)
    # db.session.commit()


def update_speed_rpm_distance(data):
    speed = int(data.get('speed'))
    rpm = int(data.get('rpm'))
    distance = int(data.get('distance'))
    socketio.emit('speed', {
        'speed': speed,
        'rpm': rpm,
    })
    socketio.emit('distance', {
        'distance': distance
    })
    # speed_rpm_distance = SensorReadings(
    #     speed=speed, rpm=rpm, distance=distance)
    # db.session.add(speed_rpm_distance)
    # db.session.commit()


def update_blinkers(data):
    socketio.emit('blinkers', {
        'blinkers': int(data.get('blinkers')),
    })
    # temp_readings = SensorReadings(temperature=temperature)
    # db.session.add(temp_readings)
    # db.session.commit()


# def update_gps(data):
#     gps_lat = data.get('gps_lat')
#     gps_long = data.get('gps_long')
    # gps_data = SensorReadings(gps_lat=gps_lat, gps_long=gps_long)
    # db.session.add(gps_data)
    # db.session.commit()


def update_range_available(data):
    hours = data.get('hours')
    average_speed = 35
    range_available = hours * average_speed
    socketio.emit('range', {
        'range': range_available
    })
    # range_available = SensorReadings(range_available=range_available)
    # db.session.add(distance_available)
    # db.session.commit()
