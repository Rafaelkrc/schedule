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
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
]
