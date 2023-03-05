from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group_post),
    path('group/<int:pk>', views.group_post_detail)
]

# path('', views.index) - Need to create an index view in the views.py file

