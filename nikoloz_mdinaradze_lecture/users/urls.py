from django.urls import path
from users.views import register, login_view, home

urlpatterns = [
    path("register/", register, name='register'),
    path("login/", login_view, name='login'),
    path("secret-home/", home, name='home')
]
