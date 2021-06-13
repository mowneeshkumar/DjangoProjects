from django.shortcuts import render
from .forms import RegisterForm,ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def homeview(request):
    return render(request,'webapp/index.html')
def aboutview(request):
    return render(request,'webapp/about.html')
def courseview(request):
    if request.method=="GET":
        form=RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name=request.POST.get('name')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            course=request.POST.get('course')
            send_mail('Mail from your website register form',
                       name+mobile+course,

                       email,
                      ['to mail'],
                      fail_silently=False,)
            return HttpResponse('<h1>success<h1>')
    return render(request,'webapp/course.html',{'form':form})
def contactview(request):
    if request.method=="GET":
        form=ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name=request.POST.get('name')
            email=request.POST.get('email')
            message=request.POST.get('message')
            send_mail('Mail from your website contact form',
                       name+message,
                       email,
                      ['to mail'],
                      fail_silently=False,)
            return HttpResponse('<h1>success<h1>')
    return render(request,'webapp/contact.html',{'form':form})

