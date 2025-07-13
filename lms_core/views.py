from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz
from .models import Enrollment, Submission,Course
from django.contrib.auth.decorators import login_required
# Create your views here.
def student_dashboard(request):
    quizzes = Quiz.objects.all()
    return render(request, 'student/dashboard.html', {'quizzes': quizzes})
def start_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'student/start_quiz.html', {'quiz': quiz, 'questions': questions})
@login_required
def student_dashboard(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    submissions = Submission.objects.filter(student=request.user)
    
    return render(request, 'lms/student_dashboard.html', {
        'enrollments': enrollments,
        'submissions': submissions,
    })
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
    return render(request, 'course_detail.html', {
        'course': course,
        'enrolled': enrolled
    })

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('lms_core:course_detail', course_id=course.id)
@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})