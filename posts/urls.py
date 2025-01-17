from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('new_post/', views.new_post, name='new_post'),
    path('<slug:slug>/', views.post_detail, name='detail'),
    path('<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
]