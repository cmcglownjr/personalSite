from django.db import models


class Testimonial(models.Model):
    reference_name = models.CharField(max_length=150)
    reference_title = models.CharField(max_length=200)
    reference_testimonial = models.TextField()
    reference_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('reference_name',)

    def __str__(self):
        return self.reference_name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    repo = models.URLField()
    demo = models.URLField(blank=True, null=True)
    screenshot = models.ImageField()
    project_created = models.DateTimeField(db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('project_created',)

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-start',)

    def __str__(self):
        return self.company


class ExperienceItem(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='experienceitems')
    bullet = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bullet
