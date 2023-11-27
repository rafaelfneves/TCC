from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .models import UserModel
from .forms import UserForm


def index(request):
    context = {}

    context["dataset"] = UserModel.objects.all()

    return render(request, "index.html", context)


def show(request, id):
    context = {}

    context["data"] = UserModel.objects.get(id=id)

    return render(request, "show.html", context)


def new(request):
    context = {}

    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()

    context["form"] = form

    return render(request, "new.html", context)


def edit(request, id):
    context = {}

    object = get_object_or_404(UserModel, id=id)

    form = UserForm(request.POST or None, instance=object)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect(f"/users/{id}")

    context["form"] = form

    return render(request, "edit.html", context)


def delete(request, id):
    context = {}

    object = get_object_or_404(UserModel, id=id)

    context["data"] = object

    if request.method == "POST":
        object.delete()

        return HttpResponseRedirect("/users")

    return render(request, "delete.html", context)
