from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':'swati','name1':'rita'}
    return render(request,'forloop.html',context=d)

def ifelse(request):
    d={'a':100,'b':200,'c':300}
    return render(request,'ifelse.html',context=d)