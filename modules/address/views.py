from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Address


def index(request):
    addresses = Address.objects.all()
    return render(request, "index.html", {"addresses": addresses})


@require_http_methods(["POST"])
def create(request):
    street = request.POST["street"]
    number = request.POST["number"]
    complement = request.POST["complement"]
    city = request.POST["city"]
    state = request.POST["state"]
    zip = request.POST["zip"]

    record = Address(
        street=street,
        number=number,
        complement=complement,
        city=city,
        state=state,
        zip=zip,
    )

    print(record)

    record.save()

    return redirect("index")


@require_http_methods(["PATCH"])
def update(request, record_id):
    street = request.POST["street"]
    number = request.POST["number"]
    complement = request.POST["complement"]
    city = request.POST["city"]
    state = request.POST["state"]
    zip = request.POST["zip"]

    record = Address.objects.get(id=record_id)

    Address(
        street=street,
        number=number,
        complement=complement,
        city=city,
        state=state,
        zip=zip,
    )

    record.save()

    return redirect("index")


@require_http_methods(["DELETE"])
def delete(request, record_id):
    record = Address.objects.get(id=record_id)

    record.delete()

    return redirect("index")
