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

from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth.views import login, logout
from  website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^index/$', views.index, name="website"),
    url(r'^add_ad/$', views.add_ad, name="add_ad"),
    url(r'^ad_details/(?P<id>\d*)', views.ad_details, name="ad_details"),
    url(r'^about/$', views.about, name="about"),
    url(r'^account/$', views.account, name="account"),
    url(r'^login/$', login, name="HM_login"),
    url(r'^logout/$', logout, {'next_page':'http://127.0.0.1:8000/index'}, name="HM_logout"),
    #url(r'^register/$', views.RegisterFormView.as_view(), name="register"),
    url(r'^house_add/$', views.house_add_ad, name="house_add"),
    url(r'^apartment_add/$', views.apartment_add_ad, name="apartment_add"),
    url(r'^garage_add/$', views.garage_add_ad , name="garage_add"),
    url(r'^parcel_add/$', views.parcel_add_ad, name="parcel_add"),
    url(r'^add_ad/(?P<pk>[0-9]+)/edit/$', views.ad_edit, name='add_ad'),
    url(r'^account/(?P<pk>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^search/$', views.search, name='search'),
    url(r'^accounts/', include('registration.backends.simple.urls'))
]#+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


