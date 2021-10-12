from django.urls import path
from .views import loginview,typography,post_single

urlpatterns=[
    path('',loginview,name='index'),
    path('typography/',typography,name='typography'),
    path('post_single/',post_single,name='post_single'),
]