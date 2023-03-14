from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'a':220,'b':100,'c':150}
    return render(request,'condition.html',d)

def loops(request):
    d={'name':'raj'}
    return render(request,'condition.html',d)