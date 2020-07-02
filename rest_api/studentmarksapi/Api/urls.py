from django.urls import path
from studentmarksapi.Api import views

## Urls for API
urlpatterns = [
    path('students_record/',views.student_record,name='students_record'),
    path('students_record/<int:unique_id>/',views.student_record_by_prn,name='student_record'),
 
]