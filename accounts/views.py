from django.shortcuts import render
import os
from django.http import HttpResponse


from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
from django.core.mail import send_mail
from datetime import datetime,time,date
import random
import pytz
#from .models import Users
def Home(request):
    if request.method=='POST':
        return render(request,'Home.html')
    else:
        return render(request,'Home.html')






def studentlogin(request):

    if request.method== 'POST':
        userid=request.POST['Userid']
        password=request.POST['password']

        user=Studentdbs.objects.filter(registernumber=userid,Password=password)
        if user is not None:
            ats=AttendanceDetails.objects.filter(registernumber=userid).count()
            pre=AttendanceDetails.objects.filter(registernumber=userid,Status='on').count()
            abs=AttendanceDetails.objects.filter(registernumber=userid,Status='off').count()
            return render(request,'StudentDetails(e).html',{'user':user,'ats':ats,'pre':pre,'abs':abs})
        else:
            messages.info(request,'invalid credentials')
            return redirect('studentlogin')

    else:
        return render(request,'studentlogin.html')    

def studentregister(request):

    if request.method == 'POST':

        pemail= request.POST['Parent email']
        otp=str(random.randint(1000,9999))
        send_mail(
        'otp verfication',
        otp,
        'attendancesystemnoreply@gmail.com',#from
        [pemail])
        request.session['name']=request.POST['UserName']
        request.session['regno']=request.POST['User id']
        request.session['dob']=request.POST['Date of Birth']
        request.session['dep']=request.POST.get('Department')
        request.session['staff']=request.POST.get('Staffname')
        print("here "+request.POST.get('Staffname'))
        request.session['email']=request.POST.get('MailId')
        request.session['phno']=request.POST.get('Phone number')
        request.session['pass']=request.POST.get('password')
        return render(request,'validateotp.html',{'otp':otp})
    else:
        staffs=Staffdbs.objects.all()
        return render(request,'studentregister.html',{'staffs':staffs})

def studentvalidate(request):
    if request.method == 'POST':
        if request.POST.get('otp')==request.POST.get('genotp'):
            fir_pass= request.session['pass']
            sec_pass=request.session['pass']
            if fir_pass==sec_pass:
                for studentitr in Studentdbs.objects.all():
                    if studentitr.registernumber==request.session['regno']:
                        messages.info(request,'Userid taken')
                        return redirect('studentregister')
                student=Studentdbs()
                student.name=request.session['name']
                #student.img=request.FILES['img']
                student.registernumber=request.session['regno']
                student.dob=request.session['dob']
                student.department= request.session['dep']
                student.Staffname=request.session['staff']
                student.Mail= request.session['email']
                student.phonenumber=request.session['phno']
                student.Password=request.session['pass']
                student.save()
                return redirect('studentlogin')
            else:
                messages.info(request,'password mismatch')
                return redirect('studentregister')
        messages.info(request,'invalid otp')
        return render(request,'studentregister.html')
    else:
        return render(request,'studentregister.html')


def get_staffs(request):
    if request.method=='get':
        dep=request.get['department']
        staffs=Staffdbs.objects.filter(Department=dep)
        list=[]
        for staff in staffs:
            list.append(staff.staffname)
        return HttpResponse(list)
    


def studentlogout(request):
    auth.logout(request)
    return redirect('logout')


def stafflogin(request):
    if request.method== 'POST':
        userid=request.POST['Staff Id']
        staffname=request.POST['Staff name']
        password = request.POST['password']
        user = Staffdbs.objects.filter(staffid=userid,Password=password)
        if user is not None:
            studs=Studentdbs.objects.filter(Staffname=staffname)
            return render(request,'StaffDetail.html',{'user':user,'studs':studs})
        else:
            messages.info(request,'invalid credentials')
            return render(request ,'stafflogin.html')

    else:
        today = datetime.now().date()
        Date=datetime.combine(today, time())
        print(Date)
        return render(request ,'stafflogin.html')    

def attendancesubmit(request):
    if request.method=='POST':
        staff_name=request.POST['staff']
        studs=Studentdbs.objects.filter(Staffname=staff_name)
        list=[]
        for stud in studs:
            list.append(AttendanceDetails(registernumber=stud.registernumber,Staffname=staff_name,Status=request.POST.get(str(stud.registernumber),'off')))
        AttendanceDetails.objects.bulk_create(list)
        #for store in list:
        #    store.save()
    
        return render(request,'Final Attendance Details.html',{'staffname':staff_name})
    else:
        return render(request,'StaffDetail.html')

        
       
def staffregister(request):

    if request.method == 'POST':
        fir_pass= request.POST['password']
        sec_pass=request.POST['password']
        if fir_pass==sec_pass:
            for staffitr in Staffdbs.objects.all():
                if staffitr.staffid==request.POST['staff Id']:
                    messages.info(request,'Staff Id taken')
                    return render(request,'staffregister.html')
            staff=Staffdbs()
            staff.staffid=request.POST.get('staff Id')
            staff.staffname=request.POST.get('Staff Name')
            staff.img=request.POST.get('fileToUpload')
            staff.Department=request.POST.get('Departments')
            staff.Gender=request.POST['Genderclass']
            staff.Mail=request.POST.get('MailId')
            staff.phonenumber=request.POST.get('Phone Number')
            staff.Password=request.POST.get('password')
            staff.save()

            return redirect('stafflogin')
        else:
            return render(request,'staffregister.html')
    else:
         return render(request,'staffregister.html')



    


def stafflogout(request):
    return redirect('/')




def adminlogin(request):
    if request.method== 'POST':
        userid=request.POST['User id']
        password = request.POST['password']

        user = auth.authenticate(userid=userid,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('adminlogin')

    else:
        return render(request,'adminlogin.html')    

def adminregister(request):

    if request.method == 'POST':
        fir_pass= request.POST['password']
        sec_pass=request.POST['password']
        if fir_pass==sec_pass:
            for adminitr in Admindbs.objects.all():
                if adminitr.Name==request.POST('User id'):
                    messages.info(request,'user id taken')
                    return render(request,'adminregister.html')
                    admin=admin()
                    admin.Institutename=request.POST['Institute Name']
                    admin.Instituteid=request.POST['Institute Id']
                    admin.Photo=request.POST['filetoupload']
                    admin.email=request.POST['MailId']
                    admin.Password=request.POST['password']
                    admin.save()

                    return render(request,'adminregister.html')
                else:
                    return render(request,'adminregister.html')
            else:
                  return render(request,'adminregister.html')
        else:
             return render(request,'adminregister.html')

    else:
         return render(request,'adminregister.html')


    


def adminlogout(request):
    auth.logout(request)
    return redirect('logout.html')



def mail(request):
    if request.method == 'POST':    
        list=[]
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%Y-%m-%d")
        staffname=request.POST.get('namestaff')
        print(d1)
        for obj in AttendanceDetails.objects.filter(Status="off",Date=d1,Staffname=staffname):
            stud=Studentdbs.objects.filter(registernumber=obj.registernumber).first()
            list.append(stud.Mail)
        for i in list:
            print(list)
        send_mail(
        'attendance details',
        'today you are absent',
        'attendancesystemnoreply@gmail.com',
        list)
        presentcount=AttendanceDetails.objects.filter(Status="on",Date=d1,Staffname=staffname).count()
        absentcount=AttendanceDetails.objects.filter(Status="off",Date=d1,Staffname=staffname).count()
        send_mail(
        'Today attendance details',
        'Today present strength=' + str(presentcount) + '\n''Today absent strength=' + str(absentcount),
        'attendancesystemnoreply@gmail.com',
        ['narmathaj872000@gmail.com'])
        return redirect('stafflogin')



    








