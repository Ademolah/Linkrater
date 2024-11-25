from django.urls import path
from . import views

app_name = 'link'


urlpatterns = [
    path('add/', views.add_link, name='add_link')
]