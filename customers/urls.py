from django.conf.urls import url
from customers import views

from django.urls import path, include

urlpatterns = [
    # url(r'^customers/$', views.customer_list),
    url(r'^customers/(?P<pk>[0-9]+)$', views.customer_detail),
    url(r'^customers', views.customer_list),
    
    path('login', views.login),
    path('register', views.register),
    path('forgot', views.forgot),
    
]
