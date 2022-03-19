from django.shortcuts import render
from .models import *
import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    return render(request,'registration.html')

def submit(request):
    if request.method=="POST":
        err=[]
        name = request.POST['name']
        phone_no = request.POST['phone-no']
        dob = request.POST['dob']
        qualification = request.POST['qualification']
        faculty_username = request.POST['faculty-username']
        faculty_password = request.POST['faculty-password']
        faculty_db=Faculty_Registration.objects.all()
        for i in faculty_db:
            if i.user_name == faculty_username:
                err.append('check_username')
                err.append('User Name already exist')
        values={
            'name':name,
            'phone_no':phone_no,
            'dob':dob,
            'qualification':qualification,
            'faculty_username':faculty_username,
            'faculty_password':faculty_password
        }
        if name=="":
            err.append('name')
            err.append('name cannot be empty')
        if phone_no=="":
            err.append('phone_no')
            err.append('phone_no cannot be empty')
        if dob=="":
            err.append('dob')
            err.append('dob cannot be empty')
        if qualification=="":
            err.append('qualification')
            err.append('qualification cannot be empty')
        if faculty_username=="":
            err.append('faculty_username')
            err.append('faculty_username cannot be empty')
        if faculty_password=="":
            err.append('faculty_password')
            err.append('faculty_password cannot be empty')
        if(err):
            err_dict={err[i]:err[i+1] for i in range(0,len(err),2)}
            data={
                'error':err_dict,
                'value':values
            }
            return render(request,'registration.html', data)
        else:
            register=Faculty_Registration(name=name,phone=phone_no,dob=dob,qual=qualification,user_name=faculty_username,password=faculty_password)
            register.save()
            return render(request,'index.html')
from django.db import connection
def login(request):
    if request.method=="POST":
        global f_name
        username = request.POST['user_id']
        f_name = username
        password=request.POST['password']
        obj=Faculty_Registration.objects.get(user_name=username)
        Pass=obj.password
        error={
            'error':"Username Or Password Doesn't match",
            'username':username
        }
        # attendence_data={
        #     'name':username,
        #     'date':datetime.datetime.now().strftime("%x")
        # }
        if password==Pass:
            stud_db=Student_DB.objects.all()
            return render(request,'studentdetails.html',{'stud':stud_db,'name':username,
            'date':datetime.datetime.now().strftime("%x")})
            # return render(request,'studentdetails.html' ,attendence_data)
        else:
            return render(request,"index.html",error)
def addstudent(request):
    if request.method=="POST":
        name = request.POST['s-name']
        rollno = request.POST['s-rollno']
        course = request.POST['course']
        semester = request.POST['semester']
        branch = request.POST['branch']
        # values={
        #     'name':name,
        #     'rollno':rollno,
        #     'course':course,
        #     'semester':semester,
        #     'branch':branch,
        # }
        add=Student_DB(name=name,rollno=rollno,course=course,semester=semester,branch=branch)
        add.save()
        # attendence_data={
        #     'name':f_name,
        #     'date':datetime.datetime.now().strftime("%x")
        # }
        stud_db=Student_DB.objects.all()
        return render(request,'studentdetails.html',{'stud':stud_db,'name':f_name,
            'date':datetime.datetime.now().strftime("%x")})

def mark_attendence(request,name,month,date,year):
        if request.method=="POST":
            year=datetime.datetime.now().strftime("%Y")
            stud_db=Student_DB.objects.all()
            for i in stud_db:
                status=request.POST['status'+str(i.sno)]
                add=Attendence_record(rollno=i.rollno,faculty=name,date=datetime.date(int(year),month,date),status=status)
                add.save()
            # print(request.POST['status1'])
            # print(request.POST['status2'])
            # print(name)
            
            # add=Attendence_record(rollno=rollno,faculty=name,date=datetime.date(year,month,date),status=status)
            # add.save()
            stud_db=Student_DB.objects.all()
            attendence=Attendence_record.objects.filter(faculty=name,date=datetime.date(int(year),month,date))
            return render(request,'studentdetails.html',{'stud':stud_db,'name':name,'date':datetime.datetime.now().strftime("%x"),'attendence':attendence,'show':'show'}) 
            
def show_attendence(request,name):
        att=Attendence_record.objects.values('date').distinct().order_by('date').reverse()
        att_all=Attendence_record.objects.filter(faculty=name)
        stud_db=Student_DB.objects.all()
        return render(request,'show_attendence.html',{'att':att,'att_all':att_all,'stud':stud_db,'name':name})