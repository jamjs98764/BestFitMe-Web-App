from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from user_profile import views

urlpatterns = [
    url(r'^form/$', views.display, name ="display")
]
