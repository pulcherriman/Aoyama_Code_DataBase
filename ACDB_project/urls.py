from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^ACDB_app/', include('ACDB_app.urls')),
]