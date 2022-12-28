from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':20,'b':30}
    return render(request,'a1_first.html',context=d)
def a1_second(request):
    e={'a':20,'b':30,'c':23}
    return render(request,'a1_second.html',context=e)