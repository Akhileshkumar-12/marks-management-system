from django.shortcuts import render,redirect
from .models import Student,Faculty,Subject
def dashboard(request):
    st_data=Student.objects.get(roll_no=st_id)
    return render(request,'NewDashboard.html',{'data':st_data})
def reportCard(request):
    st_data=Student.objects.get(roll_no=st_id)
    return render(request,'ReportCard.html',{'data':st_data})
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
