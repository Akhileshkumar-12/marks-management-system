from django.shortcuts import render,redirect
from .models import Student,Faculty,Subject

def dashboard(request):
    st_data=Student.objects.get(roll_no=st_id)
    return render(request,'NewDashboard.html',{'data':st_data})


def reportCard(request,usersub):
    st_data=Student.objects.get(roll_no=st_id)
    st_sub=Subject.objects.filter(rollNo=st_id)
    if usersub=='abc':
        marksdata=Subject.objects.get(rollNo=st_id , subjectCode=st_sub[0].subjectCode)
        subname=Faculty.objects.get(subjectCode=st_sub[0].subjectCode)
    else:
        marksdata=Subject.objects.get(rollNo=st_id, subjectCode=usersub)
        subname=Faculty.objects.get(subjectCode=usersub)
    return render(request,'ReportCard.html',{'data':st_data,'subdata':st_sub,'marksdata':marksdata,'subname':subname})


def login(request):
    error =""
    if request.method == 'POST':
       roll=request.POST['Roll_No']
       global st_id   #st_id is the id of the logged in student used in other templates (until logged out)
       st_id=roll
       error = ""
       pwd=request.POST['password']
       if Student.objects.filter(roll_no=roll,password=pwd):
           error += "success"
           
           return dashboard(request)
       else:
           error +="Try again"
           
    return render(request,'login.html',{'error':error})

def loginAsFaculty(request):
    error =""
    if request.method == 'POST':
       Faculty_Id = request.POST['Faculty_Id']
       global f_id   #f_id is the id of the logged in Faculty used in other templates (until logged out)
       f_id=Faculty_Id 
       pwd=request.POST['password']
       if Faculty.objects.filter(fId=Faculty_Id,password=pwd):
           error = "success"
           return facultydashboard(request)
       else:
           error +="Try again"
    return render(request,'loginAsfaculty.html',{'error':error})

def facultydashboard(request):
    facultyitem = Faculty.objects.get(fId=f_id)
    subCode = facultyitem.subjectCode
    allStudent = Subject.objects.filter(subjectCode = subCode)
    alldata=Subject()
    
    

    return render(request,'facultydashboard.html',{'data':alldata ,'allStudent':allStudent})
# Create your views here.
