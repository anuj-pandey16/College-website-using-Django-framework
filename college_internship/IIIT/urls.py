from django.contrib import admin
from django.urls import path
from IIIT import views 

# Format--> [path(<url> , views.<function>),name=<name you've given>]

urlpatterns = [
    path("",views.index,name='IIIT'),
    path("about",views.about,name='about'),
    path("test",views.test,name='test'),
    path("Utu",views.Utu,name='Utu'),
    path("Institude",views.Institude,name='Institude'),
    path("Facilities",views.Facilities,name='Facilities'),
    path("Course_Offered",views.Course_Offered,name='Course_Offered'),
    path("Academics",views.Academics,name='Academics'),
    path("Admission",views.Admission,name='Admission'),
    path("E_Sport",views.E_Sport,name='E_Sport'),
    path("Techno",views.Techno,name='Techno'),
    path("Drama",views.Drama,name='Drama'),
    path("music",views.music,name='music'),
    path("Technical",views.Technical,name='Technical'),
    path("event",views.event,name='event'),
    path("litrary",views.litrary,name='litrary'),
    path("Civil_Engineering",views.Civil_Engineering,name='Civil_Engineering'),
    path("Computer_Science_and_engineering",views.Computer_Science_and_engineering,name='Computer_Science_and_engineering'),
    path("Artificial_Intelligence_and_Machine_Learning",views.Artificial_Intelligence_and_Machine_Learning,name='Artificial_Intelligence_and_Machine_Learning'),
    path("Robotics_and_Automation",views.Robotics_and_Automation,name='Robotics_and_Automation'),
    path("Mechanical_Engineering",views.Mechanical_Engineering,name='Mechanical_Engineering'),
    path("login",views.login,name='login'),
    path("Fee_Structure",views.Fee_Structure,name='Fee_Structure'),
    path("Dress_code",views.Dress_code,name='Dress_code'),
    path("Faculty",views.Faculty,name='Faculty'),



]



