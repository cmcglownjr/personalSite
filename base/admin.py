from django.contrib import admin

from .models import Testimonial, Project


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['reference_name', 'reference_title', 'reference_testimonial', 'image_url', 'created']
    list_filter = ['reference_name', 'created']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'repo', 'demo', 'screenshot', 'project_created', 'created']
    list_filter = ['name', 'project_created']
