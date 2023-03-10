from django.db import models


class Testimonial(models.Model):
    reference_name = models.CharField(max_length=150)
    reference_title = models.CharField(max_length=200)
    reference_testimonial = models.TextField()
    reference_url = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.reference_name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    repo = models.URLField()
    demo = models.URLField(blank=True)
    screenshot = models.ImageField()
    project_created = models.DateTimeField(db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
