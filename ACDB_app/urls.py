from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$',RedirectView.as_view(url='/index/')),
    url(r'^index/$', views.index, name='index'),
    path('user/<str:input>', views.getUser, name='getuser'),
    path('submission/<int:id>', views.getSubmission, name='getSubmission'),
	path('submit/', views.submit, name='submit')
]