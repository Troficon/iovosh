from django.db import models
from django.utils import timezone


class Post(models.Model):
    Doctor = models.ForeignKey('auth.User')
    Zagolovok = models.CharField(max_length=200)
    Text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title