from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from user_profiles import views

urlpatterns = [
    url(r'^form/$', views.ProductSearchView.as_view(), name='products_search')
]
