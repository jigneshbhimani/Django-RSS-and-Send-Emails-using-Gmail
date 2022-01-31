from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    send_mail("Hello, I am Jignesh Bhimani",
    'Hello there, This is an automated email from Django',
    'jigneshbhimani2411@gmail.com',
    ['bomaric287@peykesabz.com'],
    fail_silently=False,
    )
    return render(request,'app/send.html')