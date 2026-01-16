from django.db import models

# Create your models here.
class AboutUs(models.Model):
    about_heading=models.CharField(max_length=30)
    about_disc=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about_heading
    
# 

class FollowUs(models.Model):
    plateform=models.CharField(max_length=30)
    link=models.URLField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plateform