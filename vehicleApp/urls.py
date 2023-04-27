from django.urls import path
from vehicleApp import views

app_name = 'vehicle'

urlpatterns = [
    path('admin-home',views.vehicle_list,name='name'),
    path('',views.vehicle_list1,name='vehicle_list'),
    path('create-vehicle/',views.vehicle_create,name='create_vehicle'),
    #path('view-vehicle/',views.vehicle_list,name='view-vehicle')
    path('delete/<int:id>/', views.delete, name="delete"),

]