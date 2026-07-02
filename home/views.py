from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
       "variable":"this is the sent"
    }
    return render(request,'index.html', context)
    #return HttpResponse("this is Homepage")


def about(request):
     return render(request,'about.html')
    #return HttpResponse("this is aboutpage")

def services(request):
     return render(request,'services.html')
    #return HttpResponse("this is Servicespage")

def contact(request):
     return render(request,'contact.html')
    #return HttpResponse("this is Contactpage")
