from django.urls import path
from . views import calculate_dist

app_name='location_app'

urlpatterns = [
     path('',calculate_dist,name='calculate_dist'),
]
