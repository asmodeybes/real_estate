from django import forms
from .models import Ad




class AdForm(forms.ModelForm):
    #title = forms.CharField(max_length=40)

    class Meta:
        model = Ad
        fields = "__all__"


