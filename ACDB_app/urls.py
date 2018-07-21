from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$',RedirectView.as_view(url='/index/')),
    url(r'^index/$', views.index, name='index'),
    path('getsource/<str:input>', views.getSource, name='getsource'),
]