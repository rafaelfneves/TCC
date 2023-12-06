from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import UserModel
from .forms import UserForm
from modules.address.forms import AddressForm


def index(request):
    context = {}

    context["dataset"] = UserModel.objects.all()

    return render(request, "index.html", context)


def login(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect(
                    reverse("dashboard")
                )  # Substitua 'dashboard' pelo nome da sua página principal após o login
            else:
                # Lógica para lidar com falhas na autenticação
                pass

    return render(request, "login.html", {"form": form})


# User & Adress Forms
def register(request):
    user_form = UserForm()
    address_form = AddressForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        address_form = AddressForm(request.POST)

        if user_form.is_valid() and address_form.is_valid():
            # Lógica para salvar os dados do usuário e endereço no banco de dados, se necessário
            user_form.save()
            address_form.save()

    return render(
        request,
        "register.html",
        {"user_form": user_form, "address_form": address_form},
    )


def show(request, id):
    context = {}

    context["data"] = UserModel.objects.get(id=id)

    return render(request, "app/user/show.html", context)


def new(request):
    context = {}

    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()

    context["form"] = form

    return render(request, "app/user/new.html", context)


def edit(request, id):
    context = {}

    object = get_object_or_404(UserModel, id=id)

    form = UserForm(request.POST or None, instance=object)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect(f"/users/{id}")

    context["form"] = form

    return render(request, "app/user/edit.html", context)


def delete(request, id):
    context = {}

    object = get_object_or_404(UserModel, id=id)

    context["data"] = object

    if request.method == "POST":
        object.delete()

        return HttpResponseRedirect("/users")

    return render(request, "app/user/delete.html", context)
