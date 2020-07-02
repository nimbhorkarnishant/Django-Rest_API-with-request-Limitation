from rest_framework import serializers
from studentmarksapi.models import Student_marks
from django.contrib.auth.models import User 


### Student Serilizer
class Student_marksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student_marks
        fields=['created','unique_id','data_structure','database','web_technology','cloud','data_science']