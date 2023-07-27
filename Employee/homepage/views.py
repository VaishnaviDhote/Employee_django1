from django.shortcuts import render
#from. models import employee
from .models import employee

# Create your views here.

def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contact.html')

def admin_login(request) :
    return render(request,'adminlogin.html')

def admincheck(request) :
    username = request.POST['textUsername']
    password = request.POST['textpassword']

    if(username=="admin" and password=="super"):
          return render(request,'welcome.html')

    else:
        return render(request, 'error.html')


def error(request):
    return render(request,'error.html')


def addemployee(request):
    # if request.POST =='POST':
    #     i = request.POST['txtEmpid']
    #     n = request.POST['txtname']
    #     m = request.POST['txtmobile']
    #     d = request.POST['txtDesignation']
    #     s = request.POST['txtsalary']
    #
    #     x = Employee(request.POST)
    #
    #     x.empid = i
    #     x.empname = n
    #     x.empmobile = m
    #     x.empdesignation = d
    #     x.empsalary = s
    #
    #     x.save()
    #

    return render(request,'adminAddEmployee.html')

 # def regsuccess(request):
 #    return render(request,'adminRegsuccess.html')