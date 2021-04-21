from django.shortcuts import render,redirect

def dashboard(request):
    return render(request,'NewDashboard.html')
def reportCard(request):
    return render(request,'ReportCard.html')
def login(request):
    # if request.method == 'POST':
       
    return render(request,'login.html')
def facultydashboard(request):
    return render(request,'facultydashboard.html')
# Create your views here.
