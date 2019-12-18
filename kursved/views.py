from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.forms import modelformset_factory
from .models import vedom, stud, studtovedom
from .forms import LogForm, StudForm

def index (request):
    if request.user.is_authenticated:
        return redirect('vedomlist')
    else:
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
            return redirect('vedomlist')
        else:
            return redirect('err')
    else:
        return redirect('err')
        
def vedomlist(request):
    if request.user.is_authenticated:
        user = request.user
        if user is not None:
            if user.is_active:
                vedom_list = vedom.objects.order_by('id')
                vedom_list = vedom_list.filter(id_user = user)
                context = {'vedom_list' : vedom_list}
                return render(request, 'kursved/vedlist.html', context)
            else:
                return redirect('err')
        else:
            return redirect('err')
    else:
        return redirect('err')

def vedomid(request, ved):
    if request.user.is_authenticated:
        studlist = studtovedom.objects.order_by('id')
        studlist = studlist.filter(vedomname = ved)
        formset = StudForm
        #formset = modelformset_factory(studtovedom, form=StudForm, extra=0)
        form = formset(queryset = studlist)
        #for form in formset.forms:
        #    form.fields['studname'].widget.attrs['readonly'] = True
        context = {'formset' : form}
        return render(request, 'kursved/vedom.html', context)
    else:
        return redirect('err')

def save(request):
    stform = StudForm
    form = stform(request.POST)
    if form.is_valid():
        form.save()
    else:
        return redirect('err')
    return redirect('vedomlist')
    
def err(request):
    return render(request, 'kursved/err.html')