from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    
    path('registro/', views.registro_usuario, name='registro'),
    path('logout/', views.logout_usuario, name='logout'),
]