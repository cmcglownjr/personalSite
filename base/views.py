from django.shortcuts import render
from taggit.models import Tag

from .models import Testimonial, Project, Experience


def home(request):
    testimonials = Testimonial.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    tags = Tag.objects.all()
    context = {
        'testimonials': testimonials,
        'projects': projects,
        'experiences': experiences,
        'tags': tags,
    }
    return render(request, 'base/index.html', context)
