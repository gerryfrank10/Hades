from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now)
    publish_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now
        self.save
    def __str__(self):
        return self.title