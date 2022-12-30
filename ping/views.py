from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ChatModel
import os
path = 'C:\\Users\\Aum Dabke\\Desktop\\django'
dir = os.listdir(path)
if 'has.qr' in dir:
    qr = True
else:
    qr=False

def login_user(request):
    if request.method=='POST':
        print(request.POST)
        if request.POST.get('password2') != None:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"Account Created Successfully for :  "+user)
                return redirect('login')
            else:
                messages.error(request,form.errors)
                print(form.errors)
                return redirect('login')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('chat')
            else:
                messages.error(request,"Invalid Username or Password")
    form = CreateUserForm()
    if 'required' in request.get_full_path():
        return render(request,'login.html',{'form':form,'login_first':"Please Login first"})
    if qr:
        return render(request,'login.html',{'form':form,'qr':True})
    else:
        return render(request,'login.html',{'form':form})

@login_required(login_url='/login/login_required')
def chat(request,**username):
    message_obj = {}
    if username:
        username_obj = User.objects.get(username=username['username'])
        if request.user.id > username_obj.id:
            thread_name = f'chat_{request.user.id}-{username_obj.id}'
        else:
            thread_name = f'chat_{username_obj.id}-{request.user.id}'
        print("[+] THREAD NAME : ",thread_name)
        message_obj = ChatModel.objects.filter(thread_name=thread_name)
    user_obj = User.objects.exclude(username=request.user.username)
    # for user in  user_obj:
    #     if user.is_superuser:
    #         user_obj.delete(user)
    print(user_obj)
    if username:
        return render(request,'chat.html',{'username_obj':username_obj,'users':user_obj,'messages':message_obj})
    
    return redirect(f'/chat/{user_obj[0]}')
    # return render(request,'chat.html',{'users':user_obj,'messages':message_obj})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/login_required')
def search(request):
    u_name = request.get_full_path().split('=')[1]
    if u_name:
        obj = User.objects.filter(username__icontains=u_name)
    else:
        obj=User.objects.exclude(username=request.user.username)
    return render(request,'search.html',{'users':obj}) 

@login_required(login_url='/login/login_required')
def user(request,user):
    obj = User.objects.filter(username__icontains=user)
    return render(request,'user.html',{'obj':obj})