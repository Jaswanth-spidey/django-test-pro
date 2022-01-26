from multiprocessing import context
from re import template
import re
from django.shortcuts import render, redirect
from crudexample.models import UserDetails
from crudexample.forms import UserForm
from django.views.generic import ListView, DetailView

# Create your views here.

'''
class IndexView(ListView):
    template_name = 'crudexample/index.html'
    context_object_name = 'user_list_dict'

    def get_queryset(self):
        return UserDetails.objects.all()
'''
'''
class UserDetailsDetailView(DetailView):
    model = UserDetails
    template_name = 'crudexample/userdetails.html'
'''


def index(request):
    user_dict = {'key':UserDetails.objects.all()}
    return render(request, 'crudexample/index.html', user_dict)


def create_user(request):
    context = {}
    form = UserForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    context['form'] = form
    return render(request, 'crudexample/create.html', context)

