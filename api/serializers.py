
from rest_framework import serializers
from .models import Patient, MedicalRecord, Appointment, Prescription

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['url', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone', 'address']

class MedicalRecordSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedRelatedField(view_name='patient-detail', read_only=True)
    
    class Meta:
        model = MedicalRecord
        fields = ['url', 'patient', 'description', 'date_created']

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedRelatedField(view_name='patient-detail', read_only=True)
    
    class Meta:
        model = Appointment
        fields = ['url', 'patient', 'date', 'reason']

class PrescriptionSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedRelatedField(view_name='patient-detail', read_only=True)
    
    class Meta:
        model = Prescription
        fields = ['url', 'patient', 'medication', 'dosage', 'date_prescribed']
