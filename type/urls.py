from django.urls import path

from type.views import page_list, add, edit, delete

urlpatterns = [
    path('list/', page_list, name='type_list'),
    path('add/', add, name='type_add'),
    path('edit/<int:id>/', edit, name='type_edit'),
    path('delete/<int:id>/', delete, name='type_delete'),

]
