import os

def populate():

    sensors = {'Battery':
                   ['if_battery_present',
                    'battery_health',
                    'battery_level',
                    'battery_plug_type',
                    'battery_status',
                    'battery_technology'],
               'Bluetooth':
                   ['bluetooth_state',
                    'bluetooth_is_discovering',
                    'scan_mode',
                    'local_address',
                    'local_name'],
               'Cellular':
                   ['network_roaming',
                    'cellid',
                    'location_area_code',
                    'mobile_country_code',
                    'mobile_network_code',
                    'network_operator',
                    'network_operator_name',
                    'network_type',
                    'service_state',
                    'signal_strength'],
               'Location':
                   ['location_provider',
                    'location_provider_enabled',
                    'location',
                    'last_known_location',
                    'geocode'],
               'Settings':
                   ['airplane_mode',
                    'ringer_silent_mode',
                    'screen_on',
                    'max_media_volume',
                    'max_ringer_volume',
                    'media_volume',
                    'ringer_volume',
                    'screen_brightness',
                    'screen_timeout'],
               'Sensor':
                   ['sensors',
                    'sensors_accuracy',
                    'light',
                    'accelerometer',
                    'magnetometer',
                    'orientation'],
               'SignalStrength':
                   ['signal_strength'],
               'WiFi':
                   ['wifi_state',
                    'connection_info',
                    'scan_results']
    }

    for sensor, sensor_attribs in sensors.items():
        s = add_sensor(sensor)
        print s.sensor_id
        if s:
            try:
                print s.sensor_name + " sensor has been added successfully!!"
                print "Adding attributes to Sensor: " + s.sensor_name
            except s.DoesNotExist:
                print "Sensor NOT found to add a Sensor Attribute"
            else:
                for attribute in sensor_attribs:
                    sa = add_sensor_attribute(s.sensor_id, attribute)
                    if sa:
                        try:
                            print sa.sensor_attribute_name + " : Sensor Attribute has been added successfully"
                        except sa.DoesNotExist:
                            print attribute + ": Adding Sensor Attribute FAILED !!"


def add_sensor_attribute(sensor_id, sensor_attribute_name):
    # print sensor_id
    sa = SensorAttribute.objects.get_or_create(sensor_id_id=sensor_id, sensor_attribute_name=sensor_attribute_name)[0]
    return sa

def add_sensor(sensor_name):
    s = Sensor.objects.get_or_create(sensor_name=sensor_name)[0]
    return s

# Start execution here!
if __name__ == '__main__':
    print "Starting Sensibility population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
    from control.models import Sensor, SensorAttribute
    populate()