from django.shortcuts import render
from django.http import HttpResponse


def if_demo(request):
    login=True
    return render(request,"if_demo.html",context={'login':login})

def ifelse_demo(request):
    login=True #after change here False
    return render(request,"ifelse_demo.html",context={'login':login,'name':'vish','a':10,'b':50})


def for_demo(request):
    return render(request,"for_demo.html",context={"items":['apple','ball','cat'],\
        'profile':{'name':"vishnu","age":27,"sal":10}})
    
