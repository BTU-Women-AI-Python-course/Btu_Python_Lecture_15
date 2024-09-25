from django.urls import path
from users.views import register, login_view, home

urlpatterns = [
    path("register/", register),
    path("login/", login_view),
    path("secret-home/", home)
]
