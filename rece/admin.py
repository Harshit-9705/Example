from django.contrib import admin
from .models import *
from django.db.models import Sum

# Register your models here.
admin.site.register(StudentId)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Subject)

class subjectMark(admin.ModelAdmin):
    list_display=['student','subject','marks']
admin.site.register(SubjectMarks,subjectMark)


class studentRank(admin.ModelAdmin):
    list_display=['student','student_rank','total','date']
    ordering = ['student_rank']
    def total(self,obj):
        mark = SubjectMarks.objects.filter(student = obj.student)
        rank = mark.aggregate(marks = Sum('marks'))
        return rank['marks'] or 0

admin.site.register(StudentRank,studentRank)