
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post"),
    path('<slug:slug>', views.post_page, name="page"),
]