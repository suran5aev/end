from django.urls import path
from apps.base.views import index, chef_detail, dish_detail

urlpatterns = [
    path ('', index, name= 'index'),
    path('chef_detail/<int:id>/', chef_detail, name='chef_detail'),
    path('dish_detail/<int:id>/', dish_detail, name='dish_detail')
          
]