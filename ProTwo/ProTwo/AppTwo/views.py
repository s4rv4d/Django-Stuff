from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.forms import User
# Create your views here.

def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    dict={'help_insert':'For signing up go to /users'}
    return render(request,'App_Two/help.html',context=dict)

def users(request):
    form = User()

    if request.method == 'POST':
        form = User(request.POST)

        if form.is_valid():
            print("first:"+form.cleaned_data["first_name"])
            print('last:'+form.cleaned_data["last_name"])
            print('email:'+form.cleaned_data["email"])
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR form invalid')
    return render(request,'App_Two/users.html',{'form':form})
