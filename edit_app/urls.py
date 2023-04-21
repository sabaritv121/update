from django.urls import path
from edit_app import  views 





urlpatterns = [
    path('crud/',  views.CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
]
