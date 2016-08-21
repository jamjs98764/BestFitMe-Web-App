"""Url definition for policies app."""

from django.conf import urls

from policies.views import life as views_life
from policies.views import health as views_health


urlpatterns = [
    urls.url(r'^life', views_life.index, name="life_index"),
    urls.url(r'^health', views_health.index, name="health_index"),
]


