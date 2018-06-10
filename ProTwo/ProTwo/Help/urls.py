from django.conf.urls import url
from Help import views

urlpatterns = [
    url('',views.index,name='index')
]
