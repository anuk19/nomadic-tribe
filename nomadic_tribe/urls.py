"""nomadic_tribe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  django.urls  import  path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('hotel-detail/<uid>/' , hotel_detail , name="hotel_detail"),
    path('profile/<id>/',profile_page,name='profile'),
    path('pay_success',pay_success,name='pay_success'),
	path('pay_cancel',pay_cancel,name='pay_cancel'),
    path('checkout_session/<hotel_name>/<hotel_price>/<user>/<checkin>/<checkout>/<rooms>/<adventure_list>/', checkout_session, name='checkout_session'),
    path('stripe_webhook/',stripe_webhook,name="stripe_webhook"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
