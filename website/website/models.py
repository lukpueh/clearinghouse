from django.db import models

# Create your models here.

# experiment_info(experiment_id, experiment_name, researcher_name, resercher_email, researcher_address, irb_officer_name, irb_officer_email)
class ExperimentInfo(models.Model):
    experiment_id = models.IntegerField(primary_key=True)
    experiment_name = models.CharField(max_length=30)
    researcher_name = models.CharField(max_length=30)
    researcher_email = models.EmailField()
    researcher_address = models.CharField(max_length=64)
    irb_officer_name = models.CharField(max_length=30)
    irb_officer_email = models.EmailField()

# sensors(sensor_id, sensor_name)
class Sensors(models.Model):
    sensor_id = models.IntegerField(primary_key=True)
    sensor_name = models.CharField(max_length=30)

# sensor_attributes(sensor_attribute_id, sensor_id, sensor_attribute_name)
# sensor_id refers sensors
class SensorAttributes(models.Model):
    sensor_attribute_id = models.IntegerField(primary_key=True)
    sensor_id = models.ForeignKey(Sensors)
    sensor_attribute_name = models.CharField(max_length=30)

# experiment_sensors(experiment_id, sensor_id, frequency, usage_policy, downloadable)
# experiment_id refers experiment_info
# sensor_id refers sensors
class ExperimentSensors(models.Model):
    experiment_sensor_id = models.IntegerField(primary_key=True)
    experiment_id = models.ForeignKey(ExperimentInfo)
    sensor_id = models.ForeignKey(Sensors)
    frequency = models.IntegerField(max_length=30)
    usage_policy = models.CharField(max_length=512)
    downloadable = models.BooleanField(default=True)

# experiment_sensor_attributes(experiment_id, sensor_attribute_id, precision)
# experiment_id refers experiment_info
# sensor_attribute_id refers sensor_attributes
class ExperimentSensorAttributes(models.Model):
    experiment_sensor_attribute_id = models.IntegerField(primary_key=True)
    experiment_id = models.ForeignKey(ExperimentInfo)
    sensor_attribute_id = models.ForeignKey(SensorAttributes)
    precision = models.IntegerField(max_length=30)

# location_blur(experiment_id, blur_level)
# experiment_id refers experiment_info
class LocationBlur(models.Model):
    BLUR_CHOICES = (
        ('city', 'City'),
        ('state', 'State'),
        ('country', 'country')
    )
    experiment_id = models.ForeignKey(ExperimentInfo)
    blur_level = models.CharField(max_length=10,
                                  choices=BLUR_CHOICES)
