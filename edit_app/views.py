from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import CrudUser
from django.views.generic import View
from django.http import JsonResponse

class CrudView(ListView):
    model = CrudUser
    template_name = 'edit_app/crud.html'
    context_object_name = 'users'




class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)    