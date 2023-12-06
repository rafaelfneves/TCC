import hashlib
import random
import string
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Voucher


def voucher_page(request):
    return render(request, "voucher.html")


@csrf_exempt
def generate_voucher(request):
    voucher_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    hashed_code = hashlib.sha256(voucher_code.encode()).hexdigest()

    # Salva o voucher no banco de dados
    Voucher.objects.create(cod_voucher=voucher_code, hashed_code=hashed_code)

    return JsonResponse({"voucher_code": voucher_code, "hashed_code": hashed_code})


@csrf_exempt
def verify_voucher(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input", "")
        voucher_code = request.POST.get("voucher_code", "")

        try:
            voucher = Voucher.objects.get(cod_voucher=voucher_code)
            hashed_user_input = hashlib.sha256(user_input.encode()).hexdigest()

            if hashed_user_input == voucher.hashed_code:
                return JsonResponse({"status": "OK"})
            else:
                return JsonResponse({"status": "Invalid"})
        except Voucher.DoesNotExist:
            return JsonResponse({"status": "Not Found"})

    return JsonResponse({"status": "Error"})
