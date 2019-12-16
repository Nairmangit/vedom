from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from .models import vedom
from .models import stud 
from .forms import LogForm


def index (request):
    form = LogForm()
    context = {'form' : form}
    return render(request, 'kursved/index.html', context)
    
def loggout (request):
    logout(request)
    form = LogForm()
    context = {'form' : form}
    return render(request, 'kursved/index.html',context)
    
@require_POST
def logg (request):
    
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            vedom_list = vedom.objects.order_by('id')
            vedom_list = vedom_list.filter(id_user = user)
            context = {'vedom_list' : vedom_list}
            return render(request, 'kursved/vedlist.html', context)
        else:
            return redirect('index')
    else:
        return redirect('index')