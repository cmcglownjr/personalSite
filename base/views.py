from django.shortcuts import render

from .models import Testimonial, Project, Experience


def home(request):
    testimonials = Testimonial.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    context = {
        'testimonials': testimonials,
        'projects': projects,
        'experiences': experiences
    }
    return render(request, 'base/index.html', context)
