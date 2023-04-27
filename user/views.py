from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User


# Create your views here.
# for admin
def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)

                return HttpResponseRedirect("/create-vehicle/")

        context = {
            "title": "Login",
            "error": True,
            "message": "Invalid username or password"
        }
        return render(request, "users/signup.html", context)
    else:
        context = {
            "title": "Login",
        }
        return render(request, "users/login.html", context)
# for user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return render(request, "users/home1.html")

                #return HttpResponseRedirect("/create-vehicle/")

        context = {
            "title": "Login",
            "error": True,
            "message": "Invalid username or password"
        }
        return render(request, "users/home1.html", context)
    else:
        context = {
            "title": "Login",

        }
        return render(request, "users/login1.html", context)

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         cpassword = request.POST['confirm_password']
#         if password == cpassword:
#             if User.objects.filter(username=username).exists():
#                 #messages.info(request, "username taken")
#                 context = {
#                     'error': True,
#                     'message': 'Username Already exists'
#                 }
#                 return render(request,'users/signup.html',context)
#                 #return redirect('myapp:register')
#             else:
#                 user = User.objects.create_user(username=username, password=password)
#                 user.is_staff = False
#                 user.save();
#                 context = {
#                     'message' : "Successfully created"
#                 }
#                 return render(request,'users/login1.html',context=context)
#         else:
#             #messages.info(request, "password not matching")
#             context = {
#                 'error': True,
#                 'message': 'Password Not Matching'
#             }
#             return render(request,'users/signup.html',context)
#             #return redirect('myapp:register')
#         return redirect('/')
#     return render(request, "users/signup.html")



 #### NEW REGISTER
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST.get('confirm_password')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                context = {
                    'error': True,
                    'message': 'Username Already exists'
                }
                return render(request, 'users/signup.html', context)
            else:
                user = User.objects.create_user(username=username, password=password)
                user.is_staff = False
                user.save();
                context = {
                    'message': "Successfully created"
                }
                return render(request, 'users/login1.html', context=context)
        else:
            context = {
                'error': True,
                'message': 'Password Not Matching'
            }
            return render(request, 'users/signup.html', context)
    return render(request, "users/signup.html")


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("user:login-user"))