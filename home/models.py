from django.db import models


class Job(models.Model):
    job = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    image = models.ImageField(max_length=2083, upload_to="img/%y")
    def __str__(self):
        return self.job

class Contact(models.Model):
    email = models.EmailField()
    description = models.TextField(max_length=1000)

class Testimonial(models.Model):
    name = models.CharField(max_length=50,default="")
    description = models.CharField(max_length=200)
