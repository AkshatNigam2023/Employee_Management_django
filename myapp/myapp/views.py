# from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    isActive = True
    if request.method=='POST':
    # check=request.POST['check']
      check=request.POST.get("check")
      print(check)
      if check is None: isActive=False
      else: isActive=True


    date = datetime.datetime.now()
    #print("Test fn is called from view")
    #return HttpResponse("<h1>Hello Akshat</h1>"+ " "+str(date)) #Sending dynamic date and time
    
    name = 'Akshat'
    list_of_programs=['WAP to check even or odd',
                      'WAP to check prime number',
                      'WAP to check all prime number from 1 to 100',
                      'WAP to print pascals triangle']
    student={
        "student_name":"Akshat",
        "student_college":"VIT",
        "student_favourite":"Kohina"
    }
    
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student':student
    }
    return render(request,"home.html",data)

def about(request):
    #return HttpResponse("<h1>This is about page</h1>")
    return render(request,"about.html",{})

def services(request):
    #return HttpResponse("<h1>This is service page</h1>")
    return render(request,"services.html",{})
