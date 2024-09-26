from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/detail/<int:contact_id>/', views.contact, name='contact'),
    path('contact/list/search/', views.search, name='search'),
]
