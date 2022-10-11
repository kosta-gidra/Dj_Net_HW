from django.urls import path

from measurement.views import SensorsCreateView, SensorsUpdateView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorsCreateView.as_view()),
    path('sensors/<pk>/', SensorsUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view())

]
