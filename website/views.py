from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AdForm
from .models import Ad
from django.views.generic.edit import CreateView
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.db import models

user=User.objects.all()

def index(request):
    return render(request, "website/index.html")


def about(request):
    return render(request, "website/About.html")

@login_required
def add_ad(request):
    form = AdForm()
    if request.method == 'POST':
        print(request.POST)
        form = AdForm(request.POST)
        print(form)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.published_date = now()
            print(ad)
            ad.save()

            return redirect("index")

    return render(request, "website/add_ad.html", {"form": form})

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


