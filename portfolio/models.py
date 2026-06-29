from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    github_link = models.URLField(max_length=200, blank=True)
    live_link = models.URLField(max_length=200, blank=True)
    description = models.TextField()
    featured = models.BooleanField(default=False)
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

