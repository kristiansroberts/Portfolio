from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    github_link = models.URLField(max_length=200, blank=True)
    live_link = models.URLField(max_length=200, blank=True)
    description = models.TextField()
    featured = models.BooleanField(default=False)
    sort_order = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='project_thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.title

class About(models.Model):
    resume_link = models.URLField(max_length=200, blank=True)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField(blank=True)

    def __str__(self):
        return "About Content"

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Contact Form Submission from {self.name}"