from django.urls import path
from .views import generate_voucher, verify_voucher
from . import views

urlpatterns = [
    path("", views.voucher_page, name="vouchers"),
    path("generate/", generate_voucher, name="generate_voucher"),
    path("verify/", verify_voucher, name="verify_voucher"),
]
