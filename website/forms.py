from django import forms
from .models import *
from django.contrib.auth.models import User

class AdForm(forms.ModelForm): #форма для квартиры
    #title = forms.CharField(max_length=40)

    class Meta:
        model = Ad
        exclude = ['dt', 'author', 'area',]
        #fields = []


class AdForm_house(forms.ModelForm): #форма для дома
    #title = forms.CharField(max_length=40)
    #category_house= models.ForeignKey(Category, verbose_name="Категория", default=1)

    class Meta:
        model = Ad

        exclude = ['floor', 'dt', 'author', 'area',]

class AdForm_garage (forms.ModelForm): #форма для гаража
    #title = forms.CharField(max_length=40)

    class Meta:
        model = Ad
        fields = ['category' , 'district', 'title', 'content', 'price', 'area', 'phone', 'email', 'image']

class AdForm_parcel (forms.ModelForm): #форма для участка
    #title = forms.CharField(max_length=40)

    class Meta:
        model = Ad
        fields = ['category', 'district', 'title', 'content', 'price', 'area', 'phone', 'email', 'image']

class SearchForm(forms.ModelForm):
    pass