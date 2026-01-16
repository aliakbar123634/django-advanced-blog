from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.dashboard , name="dashboard"),
    path('categories/' , views.categories , name='categories'),
    path('blogs/' , views.blogs , name='blogs'),
    path('blogs/add' , views.add_blogs , name='add_blogs'),
    path('blogs/edit/<int:blog_id>' , views.edit_blog , name="edit_blog"),
    path('blogs/delete/<int:blog_id>' , views.delete_blog , name="delete_blog"),
    path('categories/add' , views.add_category , name='add_category'), 
    path('categories/edit/<int:category_id>' , views.edit_category , name="edit_category"),
    path('categories/delete/<int:category_id>' , views.delete_category , name="delete_category"),
    path('users/' , views.users , name='users'),
    path('users/add' , views.add_users , name='add_users'),
    path('users/edit/<int:user_id>' , views.edit_users , name="edit_users"),
    path('users/delete/<int:user_id>' , views.delete_users , name="delete_users"),
]
