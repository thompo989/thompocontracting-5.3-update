from django.shortcuts import render
from .models import Job, Contact, Testimonial

def home(request):
    # print(request.POST)
    if request.method == 'POST':
        email = request.POST.get('email')
        description = request.POST.get('description')
        Contact.objects.create(email=email, description=description)
    jobs = Job.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'home.html', {'jobs': jobs, 'testimonials': testimonials})
