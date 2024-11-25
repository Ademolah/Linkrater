from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name= 'user/login.html'), name='login')
]