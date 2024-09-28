from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/list/search/', views.search, name='search'),

    # contact (CRUD)
    path('contact/detail/<int:contact_id>/', views.contactdetail, name='contact'),
    path('contact/update/<int:contact_id>/', views.update, name='update'),
    path('contact/delete/<int:contact_id>/', views.delete, name='delete'),
    path('contact/create/', views.create, name='create'),

    # user
    path('user/register/', views.register, name='register'),
]
