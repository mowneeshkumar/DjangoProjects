from django.db import models
COURSE_CHOICES=(
    ('HTML,CSS,JavaScript','HTML,CSS,JavaScript'),
    ('Core-Python,Python-Django','Core-Python,Python-Django'),
)
class RegisterModel(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email=models.EmailField()
    course=models.CharField(max_length=50,choices=COURSE_CHOICES)
class ContactModel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.CharField(max_length=100)
