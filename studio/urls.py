from django.urls import path

from studio.views import page_list, add, edit, delete, get_data

urlpatterns = [
    path('list/', page_list, name='studio_list'),
    path('add/', add, name='studio_add'),
    path('edit/<int:id>/', edit, name='studio_edit'),
    path('delete/<int:id>/', delete, name='studio_delete'),

]
