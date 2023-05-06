from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return HttpResponse("<h2>We Provide Services in Data Science Field</h2>")

def contact(request):
    return HttpResponse("<center><h1>Contact Us</h1></center>")
def User(request):
    return HttpResponse("<center><h1>User Login</h1></center>")

############################################################################
############################################################################

def happy(request):
    return render(request,'index.html')
def Love(request):
    return render(request,'Love.html')
def Laugh(request):
    return render(request,'Laugh.html')
def Angry(request):
    return render(request,'Angry.html')

def user_inp(request):
    if request.method == 'POST':
        a = int(request.POST['num1'])
        b = int(request.POST['num2'])

        print(a+b)
    return render(request,'User_input.html')