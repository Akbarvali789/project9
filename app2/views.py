from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':12,'b':32,'c':34}
    return render(request,'a2_first.html',context=d)

def a2_second(request):
    d={'name':'akbar'}
    return render(request,'a2_second.html',d)
