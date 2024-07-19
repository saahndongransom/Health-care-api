from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Patient
from django.contrib.auth import get_user_model

User = get_user_model()

class PatientTests(APITestCase):

    def setUp(self):
        
        self.user = User.objects.create_user(username='saah', password='samename')
        self.client.login(username='saah', password='samename')

        
        self.patient_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1980-01-01',
            'email': 'john.doe@example.com', 
            'phone': '1234567890',
            'address': '123 Main St',
        }

    def test_create_patient(self):
        url = reverse('patient-list')
        data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'date_of_birth': '1985-01-01',
            'email': 'jane.doe@example.com',  
            'phone': '0987654321',
            'address': '456 Elm St',
        }
        response = self.client.post(url, data, format='json')
        print("Create Patient Response:", response.data)  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Patient.objects.get().first_name, 'Jane')

    def test_get_patients(self):
        
        Patient.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='1980-01-01',
            email='john.doe@example.com',  
            phone='1234567890',
            address='123 Main St',
        )
        url = reverse('patient-list')
        response = self.client.get(url, format='json')
        print("Get Patients Response:", response.data)  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  

    def test_get_patient_detail(self):
        
        patient = Patient.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='1980-01-01',
            email='john.doe@example.com',  
            phone='1234567890',
            address='123 Main St',
        )
        url = reverse('patient-detail', args=[patient.id])
        response = self.client.get(url, format='json')
        print("Get Patient Detail Response:", response.data)  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'John')

    def test_update_patient(self):
        
        patient = Patient.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='1980-01-01',
            email='john.doe@example.com',  
            phone='1234567890',
            address='123 Main St',
        )
        url = reverse('patient-detail', args=[patient.id])
        updated_data = {
            'first_name': 'Johnathan',
            'last_name': 'Doe',
            'date_of_birth': '1980-01-01',
            'email': 'johnathan.doe@example.com',  # Valid email address
            'phone': '1234567890',
            'address': '123 Main St',
        }
        response = self.client.put(url, updated_data, format='json')
        print("Update Patient Response:", response.data)  # Print response data for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        patient.refresh_from_db()
        self.assertEqual(patient.first_name, 'Johnathan')

    def test_delete_patient(self):
       
        patient = Patient.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='1980-01-01',
            email='john.doe@example.com', 
            address='123 Main St',
        )
        url = reverse('patient-detail', args=[patient.id])
        response = self.client.delete(url, format='json')
        print("Delete Patient Response:", response.data)  
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Patient.objects.count(), 0) 