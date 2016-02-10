from django.conf.urls import url
from . import views
app_name = 'answer'
urlpatterns = [
    url(r'^answer/$', views.index, name='index'),
]
