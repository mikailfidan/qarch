from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.title
