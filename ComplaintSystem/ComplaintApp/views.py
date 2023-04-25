from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy

from .forms import CustomUserAuthenticationForm, CustomUserCreationForm, RegisterComplaintForm
from django.contrib.auth import login, authenticate

from .models import CustomUser, Flat, Building, Complaint
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib import messages

# Create your views here.

def index(request:HttpRequest):

    if request.user.is_authenticated:

        if request.user.groups.filter(name='Resident').exists():
            return redirect(reverse_lazy('resident_dashboard'))
        
        elif request.user.groups.filter(name='Manager').exists():
            return redirect(reverse_lazy('manager_dashboard'))

    return render(request, 'index.html')


def resident_dashboard(request:HttpRequest):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(pk = request.user.id)

        if user is not None and user.groups.filter(name='Resident').exists():
            
            flat = Flat.objects.get(resident = user)
            complaint = Complaint.objects.filter(resident = user).values()

            return render(request, 'resident/resident-dashboard.html', {'flat': flat, 'complaints':complaint})
        
    return redirect(reverse_lazy('home'))




@login_required(redirect_field_name= reverse_lazy('resident_dashboard'), login_url = reverse_lazy('resident_login'))
def view_resident_complaints(request:HttpRequest):

    user = CustomUser.objects.get(pk = request.user.id)

    if user is not None and user.groups.filter(name = "Resident").exists():

        complaints = Complaint.objects.filter(resident = user).values()
        return render(request, 'resident/resident-complaints.html', {'complaints':complaints})

    else:
        return redirect(reverse_lazy('home'))
    




@login_required(login_url = reverse_lazy('resident_login'))
def register_complaint(request:HttpRequest):
    
    # This view makes a post request to file a new complaint
    user = CustomUser.objects.get(pk = request.user.id)

    if user is not None and user.groups.filter(name = "Resident").exists():

        form = RegisterComplaintForm()

        if request.method == 'POST':

            form = RegisterComplaintForm(request.POST)

            if form.is_valid():

                comp_type = form.cleaned_data['ComplaintType']
                comp_description = form.cleaned_data['ComplaintDescription']

                Complaint.objects.create(ComplaintType = comp_type,ComplaintTime = dt.datetime.now(), ComplaintDescription = comp_description, resident = user)

                return redirect(reverse_lazy('resident_dashboard'))


        return render(request, 'resident/register-complaint.html', {'form':form})


    

def login_resident(request:HttpRequest):

    if request.method == 'POST':

        form = CustomUserAuthenticationForm(data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            if user is not None and user.groups.filter(name='Resident').exists():
                login(request, user)
                return redirect(reverse_lazy('resident_dashboard'))
            
            else:
                messages.add_message(request, messages.INFO, "Invalid credentials.")
            
    else:
        form = CustomUserAuthenticationForm()

    return render(request, 'resident/login-resident.html', {'form': form})





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

    return render(request, 'manager/login-manager.html', {'form':form})





def manager_dashboard(request:HttpRequest):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(id = request.user.id)

        if user is not None and user.groups.filter(name='Manager').exists():
            return render(request, 'manager/manager-dashboard.html')
        
    return redirect(reverse_lazy('home'))