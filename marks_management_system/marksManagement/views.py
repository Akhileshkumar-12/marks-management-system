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
    if request.method == 'POST':
       roll=request.POST['Roll_No']
       global st_id   #st_id is the id of the logged in student used in other templates (until logged out)
       st_id=roll
       pwd=request.POST['password']
       if Student.objects.filter(roll_no=roll,password=pwd):
           return dashboard(request)
    return render(request,'login.html')


def facultydashboard(request):
    alldata=Subject()
    # if request.method=='POST':

    return render(request,'facultydashboard.html',{'data':alldata})
# Create your views here.
