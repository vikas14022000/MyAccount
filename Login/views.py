from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def Home(request):
    return render(request,"Home.html")

def logout(request):
    return render(request,"logout.html")

def Contact(request):
    return render(request,"Contact.html")
def signup(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        unm=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['password']
        try:
            user=User.objects.get(username=unm)
            return render(request,'signUp.html')
        except:
            
            user=User.objects.create_user(first_name=fname,last_name=lname,username=unm,email=email,password=pwd)
            user.save()  
            return redirect('login')
    else:
        return render(request,'signUp.html')

def index(request):
    return render(request,"index.html")
def login(request):
    if request.method == 'POST':
        unm = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=unm, password= pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('loginpage')  # Replace 'home' with the name of your homepage URL
        else:
            # Handle invalid login
            pass
    return render(request, 'login.html')  # Create a corresponding HTML template

def logout_view(request):
    logout(request)
    return redirect('logout')