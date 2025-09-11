from django.db import models

# Create your models here.
class Job(models.Model):
    jobtype = [
        ("Full Time","Full Time"),
        ("Part Time","Part Time")
    ]
    
    
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=100,choices = jobtype)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacany = models.IntegerField(default = 1)
    salary = models.IntegerField(default = 0)
    experience = models.IntegerField(default = 1)
    category = models.ForeignKey('category',on_delete = models.CASCADE)
     
    def __str__(self):
        return self.title
        
    
    
class Category(models.Model):
    tpye = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.tpye
    