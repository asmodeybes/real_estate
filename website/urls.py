"""qv_metr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib import admin
from  website import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^index/$', views.index, name="website"),
    url(r'^add_ad/$', views.add_ad, name="add_ad"),
    url(r'^about/$', views.about, name="about"),
    url(r'^login/$', login, name="HM_login"),
    url(r'^logout/$', logout, {'next_page':"index"}, name="HM_logout"),
    url(r'^register/$', views.RegisterFormView.as_view(), name="register"),
]