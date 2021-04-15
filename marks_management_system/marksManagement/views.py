from django.shortcuts import render,redirect

def dashboard(request):
    return render(request,'NewDashboard.html')
def reportCard(request):
    return render(request,'ReportCard.html')
def login(request):
    return render(request,'login.html')
# Create your views here.
