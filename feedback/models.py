from django.db import models

class Feedback(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=250)
    country = models.CharField(max_length=250, blank=True, null=True)
    subject = models.CharField(max_length=250, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
