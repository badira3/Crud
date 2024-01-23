from django.shortcuts import render,redirect
from . models import Student
# Create your views here.
def index(request):
    data=Student.objects.all()
    print(data)
    context={"data":data}
    return render(request,'index.html',context)

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        print(name,age,email,gender)
        query=Student(name=name,age=age,email=email,gender=gender)
        query.save()
    return render(request,'index.html')
    
def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect("/")

def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        gender=request.POST['gender']  
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.age=age
        edit.email=email
        edit.gender=gender
        edit.save()
        return redirect("/")
    d=Student.objects.get(id=id)
    context={"d":d} 
    
    return render(request,'edit.html',context) 