from django.urls import URLPattern, path,include
from . import views

urlpatterns=[
    path('register/',views.register,name="blog-register")



]