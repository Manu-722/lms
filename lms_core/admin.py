from django.contrib import admin
from .models import Course, Enrollment, Quiz, Question, Submission  # Removed Lesson

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Submission)
