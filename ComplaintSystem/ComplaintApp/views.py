from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy

from .forms import CustomUserAuthenticationForm, CustomUserCreationForm
from django.contrib.auth import login, authenticate

from .models import CustomUser
from django.contrib.auth.models import Group


# Create your views here.

def index(request:HttpRequest):

    return render(request, 'index.html')

def resident_dashboard(request:HttpRequest):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(id = request.user.id)

        if user is not None and user.groups.filter(name='Resident').exists():
            return render(request, 'resident-dashboard.html')
        
    return redirect(reverse_lazy('home'))


def manager_dashboard(request:HttpRequest):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(id = request.user.id)

        if user is not None and user.groups.filter(name='Manager').exists():
            return render(request, 'manager-dashboard.html')
        
    return redirect(reverse_lazy('home'))

    

def login_resident(request:HttpRequest):

    if request.method == 'POST':

        form = CustomUserAuthenticationForm(data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            if user is not None and user.groups.filter(name='Resident').exists():
                login(request, user)
                return redirect(reverse_lazy('home'))
            
    else:
        form = CustomUserAuthenticationForm()

    return render(request, 'login-resident.html', {'form': form})



def login_manager(request:HttpRequest):


    if request.method == 'POST':

        form = CustomUserAuthenticationForm(data = request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email = email, password = password)

            if user is not None and user.groups.filter(name = 'Manager').exists():

                login(request, user)
                return redirect(reverse_lazy('home'))
            
    else:

        form = CustomUserAuthenticationForm()

    return render(request, 'login-manager.html', {'form':form})