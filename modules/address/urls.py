from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create, name="create"),
    path("update/<int:address_id>/", views.update, name="update"),
    path("delete/<int:address_id>/", views.delete, name="delete"),
]
