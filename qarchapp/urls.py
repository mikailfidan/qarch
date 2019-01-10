from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<det_id>', views.detail, name='detail'),
    path('sendmessage', views.sendmessage, name="sendmessage"),
    
]
