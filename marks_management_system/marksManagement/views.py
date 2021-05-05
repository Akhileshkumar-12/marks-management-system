from django.shortcuts import render,redirect
from .models import Student,Faculty,Subject,Sem_Grade
# from json import dumps

def dashboard(request):
    st_data=Student.objects.get(roll_no=st_id)
    subjectsdata=Subject.objects.filter(rollNo=st_id)
    # totalmarks=0
    # for i in range(len(subjectsdata)):
    #     totalmarks+=(subjectsdata[i].total/200)
    # totalmarks/=len(subjectsdata)
    # totalmarks*=100
    # totalmarks=round(totalmarks,2)
    semdata=Sem_Grade.objects.filter(rollNo=st_id).order_by('Sem')
    sgpa=[]
    for data in semdata:
        sgpa.append(data.sgpa)
    # semdata=dumps(semdata)
    totalcredit=0
    totalgradepoint=0
    for i in semdata:
        totalcredit+=i.totcredit
        totalgradepoint+=(i.sgpa*i.totcredit)
    cgpa=totalgradepoint/totalcredit
    cgpa=round(cgpa,2)
    return render(request,'NewDashboard.html',{'data':st_data,'totalmarks':totalcredit,'semdata':sgpa,'cgpa':cgpa})


def reportCard(request,usersub):
    st_data=Student.objects.get(roll_no=st_id)
    st_sub=Subject.objects.filter(rollNo=st_id)
    if usersub=='abc':
        marksdata=Subject.objects.get(rollNo=st_id , subjectCode=st_sub[0].subjectCode)
        sortedmarksdata=Subject.objects.filter(subjectCode=st_sub[0].subjectCode).order_by('total')
        for i in range(len(sortedmarksdata)):
            if sortedmarksdata[i].rollNo==st_id:
                k=i
                break
        marks=sortedmarksdata[k].total
        while marks==sortedmarksdata[k].total:
            k-=1
        k+=1
        percentile=len(sortedmarksdata)-k
        percentile/=len(sortedmarksdata)
        percentile*=100
        gradepoint=float(marksdata.total)//20
        Weightage=0
        if marksdata.assignment1!=0:
            Weightage+=5
        if marksdata.assignment2!=0:
            Weightage+=5
        if marksdata.classtest1!=0:
            Weightage+=7.5
        if marksdata.classtest2!=0:
            Weightage+=7.5
        if marksdata.midTerm!=0:
            Weightage+=25
        if marksdata.endTerm!=0:
            Weightage+=50    
        subname=Faculty.objects.get(subjectCode=st_sub[0].subjectCode)
    else:
        marksdata=Subject.objects.get(rollNo=st_id, subjectCode=usersub)
        Weightage=0
        if marksdata.assignment1!=0:
            Weightage+=5
        if marksdata.assignment2!=0:
            Weightage+=5
        if marksdata.classtest1!=0:
            Weightage+=7.5
        if marksdata.classtest2!=0:
            Weightage+=7.5
        if marksdata.midTerm!=0:
            Weightage+=25
        if marksdata.endTerm!=0:
            Weightage+=50 
        gradepoint=float(marksdata.total)/20
        sortedmarksdata=Subject.objects.filter(subjectCode=st_sub[0].subjectCode).order_by('-total')
        
        for i in range(len(sortedmarksdata)):
            if sortedmarksdata[i].rollNo==st_id:
                k=i
                break
        marks=sortedmarksdata[k].total
        while marks==sortedmarksdata[k].total:
            k-=1
        k+=1
        percentile=len(sortedmarksdata)-k
        percentile/=len(sortedmarksdata)
        percentile*=100
        subname=Faculty.objects.get(subjectCode=usersub)
    percentile=round(percentile,2)
    return render(request,'ReportCard.html',{'data':st_data,'subdata':st_sub,'marksdata':marksdata,'subname':subname,'gradepoint':gradepoint,'weightage':Weightage,'percentile':percentile})


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
           s="abc"
           return facultydashboard(request)
       else:
           error +="Try again"
    return render(request,'loginAsfaculty.html',{'error':error})

def facultydashboard(request):
    
    if request.method == 'POST':
        roll = request.POST.get('rol')
        sCode = request.POST.get('subCode')
        A1 = request.POST.get('a1')
        A2 = request.POST.get('a2')
        C1 = request.POST.get('c1')
        C2 = request.POST.get('c2')
        mT = request.POST.get('mt')
        eT = request.POST.get('et')
        if roll!=None and Subject.objects.get(rollNo=roll,subjectCode=sCode):
            update = Subject.objects.get(rollNo=roll,subjectCode=sCode)
            update.assignment1 = A1
            update.assignment2 = A2
            update.classtest1 = C1
            update.classtest2 = C2
            update.midTerm = mT
            update.endTerm = eT
            update.total=int(A1)+int(A2)+int(C1)+int(C2)+int(mT)+int(eT)
            update.save()
        # else:
        #     error = "error occured!! Try again"
        #     facultyitem = Faculty.objects.get(fId=f_id)
        #     subCode = facultyitem.subjectCode
        #     allStudent = Subject.objects.filter(subjectCode = subCode)
        #     alldata=Subject()
        #     st = Student.objects.all()
        #     return render(request,'facultydashboard.html',{'data':alldata ,'allStudent':allStudent,'student':st})
            
    facultyitem = Faculty.objects.get(fId=f_id)
    subCode = facultyitem.subjectCode
    allStudent = Subject.objects.filter(subjectCode = subCode).order_by('rollNo')
    # for i in range(len(allStudent)):
    #     print(allStudent[i].classtest1)
    alldata=Subject()
    st = Student.objects.all()   
    return render(request,'facultydashboard.html',{'data':alldata ,'allStudent':allStudent,'student':st,'faculty':facultyitem})
# Create your views here.