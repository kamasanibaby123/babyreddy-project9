from django.shortcuts import render

# Create your views here.
def app2_first(request):
    d={'a':50,'b':25,'c':60}
    return render(request,'app2_first.html',d)



def app2_second(request):
    d={'name':'peeyush reddy'}
    return render(request,'app2_second.html',d)
