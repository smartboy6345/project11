from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'a':420,'b':900,'c':440}
    return render(request,'IF_Elif.html',d)