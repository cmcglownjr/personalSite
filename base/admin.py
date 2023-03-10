from django.contrib import admin

from .models import Testimonial, Project, Experience, ExperienceItem


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['reference_name', 'reference_title', 'reference_testimonial', 'image_url', 'created']
    list_filter = ['reference_name', 'created']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'repo', 'demo', 'screenshot', 'project_created', 'created']
    list_filter = ['name', 'project_created']


class ExperienceItemInline(admin.TabularInline):
    model = ExperienceItem


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [
        ExperienceItemInline,
    ]
    list_display = ['company', 'location', 'title', 'start', 'end']
    list_filter = ['company', 'location', 'start', 'end']
