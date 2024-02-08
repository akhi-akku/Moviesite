from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Create your views here.
class UserDetailView(DetailView):
    model=User
    template_name = 'detail.html'
    context_object_name = 'profile'

class UserEditView(UpdateView):
    model=User
    template_name = 'update.html'
    # context_object_name = 'profile'
    fields = ['username','first_name','last_name','email','password']
    success_url = reverse_lazy('movieapp:AllProdCat')

def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=uname,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('movieapp:AllProdCat')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('credentials:login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        uname = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username already exist!!")
                return redirect("credentials:register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email id already exist!!")
                return redirect("credentials:register")
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
                user.save
                messages.info(request, "Welcome to India's No.1 Movie Hub")
                return redirect('credentials:login')
            # print("Welcome to India's No.1 Movie Hub")

        else:
            messages.info(request,"Password not matching!!")
            return redirect("/")


    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('movieapp:AllProdCat')

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")



