
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    # Страница входа.
    path('login/', views.login_view, name='login'),
    # Страница выхода из системы.
    path('logout/', views.logout_view, name='logout'),
    # Страница регистрации.
    path('register/', views.register, name='register'),
]
