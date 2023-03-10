from django.shortcuts import render

from .models import Testimonial, Project


def home(request):
    testimonials = Testimonial.objects.all()
    projects = Project.objects.all()
    return render(request, 'base/index.html', {'testimonials': testimonials, 'projects': projects})
