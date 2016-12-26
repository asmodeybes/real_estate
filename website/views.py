from django.shortcuts import render
from django.http import HttpResponse
from .forms import AdForm
from .models import Ad
from django.views.generic.edit import CreateView
from django.utils.timezone import now

def index(request):
    return render(request, "website/index.html")


def about(request):
    return render(request, "website/About.html")

def add_ad (request):


    if request.method == 'POST':
        form = AdForm()
        context = {"form": form}
        return render(request, "website/add_ad.html", context)

        if form.is_valid():
            ad = form.save(commit=False)
            ad.published_date = now()
            ad.save()
            object=Ad.objects.all()
            print(object)
            return index(request)

    form = AdForm()
    return render(request, "website/add_ad.html", {"form": form})





# class AdCreate(CreateView):
#     model = Ad
#     template_name = "add_ad"
    #success_url = "index"