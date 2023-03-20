from django.urls import path

from measurement.views import ListCreateSensorView, UpdateSensorView, AddMeasurementView

urlpatterns = [
    path('sensors/', ListCreateSensorView.as_view()),
    path('sensors/<pk>/', UpdateSensorView.as_view()),
    path('measurements/', AddMeasurementView.as_view()),
]
