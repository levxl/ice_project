from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("filter/", views.FilterIceView.as_view(), name='filter'),
    path('catalog/', views.IceView.as_view(), name='catalog'),
    path("search/", views.Search.as_view(), name='search'),
]
 