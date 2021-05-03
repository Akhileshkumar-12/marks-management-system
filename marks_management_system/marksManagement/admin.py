from django.contrib import admin
from .models import Student , Faculty , Subject,Sem_Grade

# Register your models here.
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Subject)
admin.site.register(Sem_Grade)


