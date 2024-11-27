from django.urls import path
from . import views

app_name = 'link'


urlpatterns = [
    path('add/', views.add_link, name='add_link'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/add/', views.add_review, name='add_review'),
]