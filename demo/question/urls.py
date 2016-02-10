from django.conf.urls import url
from . import views
app_name = 'question'
urlpatterns = [
    url('$', views.index, name='index'),
]
