from rest_framework import serializers
from doctor.models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

class bookedAppoimentserilizers(serializers.ModelSerializer):
    class Meta():
        model=BookedAppoiments
        fields='__all__'

class Patientserilizers(serializers.ModelSerializer):
    class Meta():
        model=Patient
        fields='__all__'



class doctorsserilizer(serializers.ModelSerializer):
    class Meta:
        model=doctors
        fields='__all__'

class doctorinfoserilizer(serializers.ModelSerializer):
    class Meta:
        model=DoctorInfo
        fields='__all__'


class DoctorsAppointmentserilizer(serializers.ModelSerializer):
    class Meta:
        model=DoctorsAppointment
        fields='__all__'




class Vaccineserilizer(serializers.ModelSerializer):
    class Meta:
        model=Vaccine
        fields='__all__'



class VaccineLocationsserilizer(serializers.ModelSerializer):
    class Meta:
        model=VaccineLocations
        fields = '__all__' 

