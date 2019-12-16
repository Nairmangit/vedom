from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from .models import vedom
from .models import stud 
from .forms import LogForm, StudForm

def index (request):
    form = LogForm()
    context = {'form' : form}
    return render(request, 'kursved/index.html', context)
    
def loggout (request):
    logout(request)
    return redirect ('index')
    
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
        
def vedomid(request, ved_id):
    studlist = stud.objects.order_by('id')
    studlist = studlist.filter(id_vedom = ved_id)
    formset = StudForm.form()
    form = formset(queryset = studlist)
    context = {'studlist' : studlist, 'form' : form}
    return render(request, 'kursved/vedom.html', context)

def save(request):
    stform = StudForm.form()
    form = stform(request.POST)
    if form.is_valid():
        form.save()
    return redirect('index')