from django.db import models


# Create your models here.
### Student Marks Model
class Student_marks(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    unique_id=models.IntegerField(default=None,unique=True)
    data_structure=models.IntegerField(default=None)
    database=models.IntegerField(default=None)
    web_technology=models.IntegerField(default=None)
    cloud=models.IntegerField(default=None)
    data_science=models.IntegerField(default=None)

#### Request count
class request_counter(models.Model):
    service_name=models.CharField(max_length=100,blank=True,null=True)
    counter_req=models.IntegerField(default=None)
