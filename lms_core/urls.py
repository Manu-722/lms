from django.urls import path
from . import views
app_name = 'lms_core'
urlpatterns = [
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('quiz/<int:quiz_id>/', views.start_quiz, name='start_quiz'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/enroll/', views.enroll_course, name='enroll_course'),
    path('courses/', views.course_list, name='course_list'),
]
