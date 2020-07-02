## Require Libraries
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,throttle_classes
from studentmarksapi.models import Student_marks
from studentmarksapi.models import request_counter
from studentmarksapi.Api.serializer import Student_marksSerializer
from rest_framework.authtoken.models import Token
from rest_framework.throttling import UserRateThrottle




#### Fetching record of all students marks
@api_view(['GET'])
@throttle_classes([UserRateThrottle])
def student_record(request):
    if request.method=="GET":
        try:
            request_counter_obj=request_counter.objects.get(service_name='request_count')
            request_counter_obj.counter_req=request_counter_obj.counter_req + 1
            request_counter_obj.save()
            students=Student_marks.objects.all()
            serializer=Student_marksSerializer(students,many=True)
            return Response(serializer.data)
        except:
            response={"message":["Record Not Found."]}
            return Response(response)


### Fetching record on the basis of unique ID
@api_view(['GET'])
@throttle_classes([UserRateThrottle])
def student_record_by_prn(request,unique_id):
    if request.method=="GET":
        try:
            request_counter_obj=request_counter.objects.get(service_name='request_count')
            request_counter_obj.counter_req=request_counter_obj.counter_req + 1
            request_counter_obj.save()
            student=Student_marks.objects.get(unique_id=unique_id)
            serializer=Student_marksSerializer(student)
            return Response(serializer.data)
        except:
            response={"message":["Record Not Found."]}
            return Response(response)
        
