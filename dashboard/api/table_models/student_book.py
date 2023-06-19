from django.db import models
from .student import Student
from .book import Book

class StudentBook(models.Model):
    sid = models.ForeignKey(Student, on_delete=models.CASCADE)
    bid = models.ForeignKey(Book, on_delete=models.CASCADE)
    ability = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    discrimination = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    difficulty = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    number_of_attempts = models.IntegerField(default=0)
    number_of_hints = models.IntegerField(default=0)
    number_of_incorrect_attempts = models.IntegerField(default=0)
    timespent = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    enroll_year = models.DateField()
    
    class Meta:
        managed = True
        db_table = 'STUDENT_BOOK'
