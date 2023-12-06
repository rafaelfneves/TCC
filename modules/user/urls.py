from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<id>", views.show, name="show"),
    path("new/", views.new, name="new"),
    path("edit/<id>", views.edit, name="edit"),
    path("delete/<id>", views.delete, name="delete"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
]
