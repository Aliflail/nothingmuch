from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'question/login.html'}),
    url(r'^create/$', views.createTest, name='question/createTest.html'),
]
