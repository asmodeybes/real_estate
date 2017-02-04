from django.shortcuts import  redirect
from time import time
from datetime import  timedelta
from django.http import HttpResponse
from .forms import *
from .models import Ad
from django.views.generic.edit import CreateView
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,InvalidPage, EmptyPage
import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

user=User.objects.all()


def index(request):
    ads_del = Ad.objects.filter(dt__lte=datetime.datetime.now()).delete()
    ads = Ad.objects.all().order_by("-published_date")
    print(ads_del)
    paginator = Paginator(ads.order_by("-published_date"), 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        p_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        p_list = paginator.page(paginator.num_pages)

    context = {'ads': ads, 'p_list':p_list}
    return render(request, "website/index.html", context )


def search(request):
    #print(request.POST)
    category = request.POST.get('category')
    descrict=request.POST.get('descrict')
    operation=request.POST.get('operation')
    price_start = request.POST.get('price_start')
    if price_start   =="" or None or not price_start.isdigit() or len(price_start)>7:
        price_start="0"
    price_finish = request.POST.get('price_finish')
    if price_finish =="" or None or not price_finish.isdigit() or len(price_finish)>7:
        price_finish= "0"
    rooms = request.POST.get('rooms')
    if rooms  == "" or None or not price_finish.isdigit() or len(rooms)>3:
        rooms = "0"
    #kitchen_area = request.POST.get('kitchen_area')
    #total_area = request.POST.get('total_area')

    print(category, descrict, operation, price_start, price_finish, rooms )

    ads = Ad.objects.filter(category__name=category, district__name=descrict, operation__name=operation, price__gte= price_start, price__lte=price_finish, rooms=rooms)
    paginator = Paginator(ads.order_by("-published_date"), 20)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        p_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        p_list = paginator.page(paginator.num_pages)

    context = {'ads':ads, 'p_list': p_list}
    return render(request, "website/index.html", context)






def about(request):
    return render(request, "website/About.html")



def account(request, id=None):
    user_id = request.user.pk
    print(user_id)
    ads = Ad.objects.filter(author_id=user_id, dt__gte=datetime.datetime.now())
    ads_del = Ad.objects.filter(author_id=user_id, dt__lte=datetime.datetime.now()).delete()
    ads_c=ads.count()

    context = {'ads': ads, 'ads_c':ads_c}
    return render(request, "website/account.html", context)



def ad_details(request, id=None):
    ads = Ad.objects.filter(pk=id)
    context = {'ads': ads}
    return render(request, "website/ad_details.html", context)


@login_required
def add_ad(request):
    form = AdForm()
    if request.method == 'POST':
        print(request.POST)
        form = AdForm(request.POST, request.FILES)
        #print(form)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.published_date = now()
            ad.dt = ad.published_date + datetime.timedelta(days=7)
            ad.author = request.user
            ad.save()

            return redirect("index")

    return render(request, "website/add_ad.html", {"form": form})

# def house_add (request):
#     ads = Ad.objects.all()
#     context = {'ads': ads}
#     return render(request, "website/index.html", context)




def house_add_ad (request):
    form = AdForm_house()
    if request.method == 'POST':
        print(request.POST)
        form = AdForm_house(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.published_date = now()
            ad.dt = ad.published_date + datetime.timedelta(days=7)
            ad.author=request.user
            if ad.email != request.user.email:
                print(' неправильный адрес')

            else:
                ad.save()
                #messages.add_message(request, messages.SUCCESS,"Товар успешно добавлен в список")
            return redirect("index")

    return render(request, "website/house_add.html", {"form": form})


def garage_add_ad (request):
    form = AdForm_garage()
    if request.method == 'POST':
        print(request.POST)
        form = AdForm_garage(request.POST, request.FILES)
        #print(form)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.published_date = now()
            ad.dt = ad.published_date + datetime.timedelta(days=7)
            ad.author = request.user
            ad.save()

            return redirect("index")

    return render(request, "website/garage_add.html", {"form": form})




def parcel_add_ad (request):
    form = AdForm_parcel ()
    if request.method == 'POST':
        print(request.POST)
        form = AdForm_parcel(request.POST, request.FILES)
        #print(form)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.published_date = now()
            ad.dt = ad.published_date + datetime.timedelta(days=7)
            ad.author = request.user
            ad.save()
            return redirect("index")

    return render(request, "website/parcel_add.html", {"form": form})



def apartment_add_ad (request):
    form = AdForm ()
    if request.method == 'POST':
        print(request.POST)
        form = AdForm(request.POST, request.FILES)
        #print(form)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.published_date = now()
            ad.dt = ad.published_date + datetime.timedelta(days=7)
            ad.author = request.user
            ad.save()

            return redirect("index")

    return render(request, "website/apartment_add.html", {"form": form})

def ad_edit(request,pk ):
        ad = get_object_or_404(Ad, pk=pk)
        ad.image = get_object_or_404(Ad, pk=pk)
        ad.delete()

        if request.method == "POST":
            form = AdForm(request.POST, request.FILES, instance=ad)

            if form.is_valid():
                ad.published_date = now()
                ad.dt = ad.published_date + datetime.timedelta(days=7)
                ad.author = request.user
                ad.image=get_object_or_404(Ad, pk=pk)
                ad.save()
                return redirect("index", pk=ad.pk)
        elif ad.category_id==1:
            form = AdForm_house(instance=ad)
            return render(request, "website/house_add.html", {"form": form})
        elif ad.category_id==2:
            form = AdForm(instance=ad)
            return render(request, "website/apartment_add.html", {'form': form})
        elif ad.category_id == 3:

            form = AdForm_garage(instance=ad)
            return render(request, "website/garage_add.html", {'form': form})
        elif ad.category_id == 4:
            form = AdForm_parcel (instance=ad)
            return render(request, "website/parcel_add.html", {'form': form})


def delete (request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    ad.delete()
    return redirect("account")



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

