# api/urls.py
from django.urls import path
from .views import (PatientListCreateView, PatientDetailView, MedicalRecordListCreateView, MedicalRecordDetailView,
                    AppointmentListCreateView, AppointmentDetailView, PrescriptionListCreateView, PrescriptionDetailView ,PatientListView, PatientDetailView)

urlpatterns = [
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('medical-records/', MedicalRecordListCreateView.as_view(), name='medical-record-list-create'),
    path('medical-records/<int:pk>/', MedicalRecordDetailView.as_view(), name='medical-record-detail'),
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('prescriptions/', PrescriptionListCreateView.as_view(), name='prescription-list-create'),
    path('prescriptions/<int:pk>/', PrescriptionDetailView.as_view(), name='prescription-detail'),
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
]
