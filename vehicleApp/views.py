from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from vehicleApp.forms import VehicleForm
from django.contrib import messages
from vehicleApp.models import Vehicle
# Create your views here.


# def home(request):
#
#     return render(request,'home.html')

@login_required(login_url="/users/login-admin/")
def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle created successfully')
            return redirect('/')
        else:
            form = VehicleForm()
            context = {
                'message' : 'please fill required form'
            }
    else:
        form = VehicleForm()
        context = {
            'form' : form
        }
        return render(request, 'form.html', context=context)

@login_required(login_url="/users/login-user/")
def vehicle_list(request):
    vehicle = Vehicle.objects.all()
    context = {
        'vehicle' : vehicle
    }
    return render(request,'home.html',context=context)

@login_required(login_url="/users/register-user/")
def vehicle_list1(request):
    vehicle = Vehicle.objects.all()
    context = {
        'vehicle' : vehicle
    }
    return render(request,'users/home1.html',context=context)


@login_required(login_url="/users/login-admin/")
def delete(request, id):
    instance = get_object_or_404(Vehicle,id=id)
    instance.delete()
    return redirect('/')

