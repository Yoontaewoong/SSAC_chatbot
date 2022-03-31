from ossaudiodev import SNDCTL_DSP_BIND_CHANNEL
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]