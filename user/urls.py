from django.urls import path
from django.contrib.auth.views import LoginView, redirect_to_login
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name= 'user/login.html'), name='login'),
    path('logout/', redirect_to_login, name='logout')
]