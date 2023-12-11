from django.urls import path
from . import views
from .views import user_login

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", user_login, name="user_login"),
]
