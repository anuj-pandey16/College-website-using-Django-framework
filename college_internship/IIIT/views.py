from django import forms
from django.shortcuts import render, HttpResponse
from IIIT.models import forms

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("This is about page")
def test(request):
    return render(request,'test.html')

def Utu(request):
    return render(request,'Utu.html')
    
def Institude(request):
    return render(request,'Institude.html')

def Facilities(request):
    return render(request,'Facilities.html')
  
def Course_Offered(request):
    return render(request,'Course_Offered.html')

def Academics(request):
    return render(request,'Academics.html')

def Admission(request):
    if request.method == "POST":
        Name = request.POST['name']
        Email = request.POST['email']
        Phone = request.POST['phone']
        Gender = request.POST['gender']
        dob_nm = request.POST['Dob_name']
        State = request.POST['State']
        add_name = request.POST['add_name']
        Pincode = request.POST['pincode']
        adm_nm = request.POST['adm_name']
        Course = request.POST['Course']
        # print(form_name,email,phone,gender,dob,state,add,pincode,adm,course)
        submission= forms(form_name=Name,email=Email,phone=Phone,gender=Gender,dob=dob_nm,state=State,add=add_name,pincode=Pincode,adm=adm_nm,course=Course)
        submission.save()
    return render(request,'Admission.html')

def E_Sport(request):
    return render(request,'E_Sport.html')

def Techno(request):
    return render(request,'Techno.html')

def Drama(request):
    return render(request,'Drama.html')

def music(request):
    return render(request,'music.html')

def Technical(request):
    return render(request,'Technical.html')

def event(request):
    return render(request,'event.html')

def litrary(request):
    return render(request,'litrary.html')

def Civil_Engineering(request):
    return render(request,'Civil_Engineering.html')

def Computer_Science_and_engineering(request):
    return render(request,'Computer_Science_and_engineering.html')

def Artificial_Intelligence_and_Machine_Learning(request):
    return render(request,'Artificial_Intelligence_and_Machine_Learning.html')

def Robotics_and_Automation(request):
    return render(request,'Robotics_and_Automation.html')

def Mechanical_Engineering(request):
    return render(request,'Mechanical_Engineering.html')

def login(request):
    return render(request,'login.html')

def Fee_Structure(request):
    return render(request,'Fee_Structure.html')

def Dress_code(request):
    return render(request,'Dress_code.html')

def Faculty(request):
    return render(request,'Faculty.html')

    