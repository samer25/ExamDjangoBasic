from django.urls import path

import recipes.views as views

urlpatterns = [
    path('', views.home_page, name='home page'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('details/<int:pk>', views.details, name='details'),

]
