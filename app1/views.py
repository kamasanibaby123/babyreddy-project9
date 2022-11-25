from django.shortcuts import render

# Create your views here.
def app1_first(request):
    d={'a':200,'b':400,}
    return render(request,'app1_first.html',d)





def app1_second(request):
    d={'a':200,'b':400,'c':300}
    return render(request,'app1_second.html',d)