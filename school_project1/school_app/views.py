from django.shortcuts import render,redirect
from.models import Student 

    
def about_page(request):
    return render(request, 'school/about.html' )
def contact_page(request):
    return render(request, 'school/contact.html')
def register_student(request):
    if request.method=="POST":
        
        name=request.POST.get("name")
        
        email=request.POST.get("email")
        country=request.POST.get("country")
        phonenumber=request.POST.get("phonenumber")
        document=request.FILES.get('document')

        student=Student.objects.create(name=name,email=email,country=country,phonenumber=phonenumber,document=document)
        student.save()
        return redirect("HOME")
    return render(request,"school/form.html")
def success_page(request):
    return render(request,'school/success.html')

# Create your views here.
