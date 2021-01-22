from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=30, default='')
    category = models.CharField(max_length=30)
    client = models.CharField(max_length=100)
    project_date = models.DateTimeField()
    project_url = models.URLField()
    project_description = models.TextField()
    github_link = models.URLField()

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='projects', on_delete=models.CASCADE)
    project_image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.project.title

class About(models.Model):
    full_name = models.CharField(max_length=100)
    job_name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=50)
    full_description = models.TextField()
    website = models.URLField()
    phone = models.CharField(max_length=15)
    my_address = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.full_name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name


class SocialProfile(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()

    def __str__(self):
        return self.name
