from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("<em>My Second App</em>")

    my_dict={'insert_me': "Hello, I'm from views.py"}
    return render(request,'AppTwo/index.html',context=my_dict)

def help(request):
    help_dict={'help_insert': "Help Page"}
    return render(request,'AppTwo/help.html',context=help_dict)