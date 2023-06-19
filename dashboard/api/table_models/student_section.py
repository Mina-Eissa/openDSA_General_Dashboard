from django.db import models
from .student import Student
from .section import Section

class StudentSection(models.Model):
    sid = models.IntegerField(default=0, blank=False)
    secid = models.IntegerField(default=0, blank=False)
    ability = models.DecimalField(max_digits=20, decimal_places=10, default=0, blank=False)
    discrimination = models.DecimalField(max_digits=20, decimal_places=10, default=0, blank=False)
    difficulty = models.DecimalField(max_digits=20, decimal_places=10, default=0, blank=False)
    number_of_attempts = models.IntegerField(default=0, blank=False)
    number_of_hints = models.IntegerField(default=0, blank=False)
    number_of_incorrect_attempts = models.IntegerField(default=0, blank=False)
    timespent = models.DecimalField(max_digits=20, decimal_places=10, default=0, blank=False)
    enroll_year = models.DateField(blank=False)
    
    class Meta:
        managed = True
        db_table = 'STUDENT_SECTION'
