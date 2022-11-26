from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse

from system.views import is_auth, is_login
from type.models import Type


@is_login
@is_auth
def page_list(request):
    types = Type.objects.all()
    page_obj = Paginator(types, per_page=5)
    page = request.GET.get('page', 1)
    try:
        types_page_obj = page_obj.page(page)
        types = types_page_obj.object_list
    except Exception as e:
        types_page_obj = page_obj.page(1)
        types = types_page_obj.object_list

        # typesPageObj=None
    return render(request, 'type/list.html', context={
        'types': types,
        'typesPageObj': types_page_obj
    })


@is_login
@is_auth
def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        _type = Type(name=name)
        _type.save()
        return redirect(reverse('type_list'))
    return render(request, 'type/add.html')


@is_login
@is_auth
def edit(request, id):
    _type = get_object_or_404(Type, id=id)

    if request.method == 'POST':
        name = request.POST.get('name', None)
        _type.name = name
        _type.save()
        return redirect(reverse('type_list'))

    return render(request, 'type/edit.html', context={
        'type': _type
    })


@is_login
@is_auth
def delete(request, id):
    _type = get_object_or_404(Type, id=id)
    _type.delete()
    return redirect(reverse('type_list'))
