from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def projects(request):
    return render(request, "pages/projects.html")

def contact(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New Contact Message from {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            email,   # sender
            ["julussy46j@nsuk.edu.ng"],  
            fail_silently=False,
        )

        context = {
            "name": name,
            "email": email,
            "message": message,
            "submitted": True,
        }

    return render(request, "pages/contact.html",context)
