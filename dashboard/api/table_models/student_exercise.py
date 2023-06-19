from django.db import models
from .section import Section
from .chapter import Chapter
from .book import Book

class StudentExercise(models.Model):
    exid = models.IntegerField(default=0, blank=False)
    sid = models.IntegerField(default=0, blank=False)
    number_of_attempts = models.IntegerField(default=0, blank=False)
    number_of_hints = models.IntegerField(default=0, blank=False)
    number_of_incorrect_attempts = models.IntegerField(default=0, blank=False)
    solved = models.BooleanField(default=False)
    ability = models.DecimalField(max_digits=20, decimal_places=10, default=0, blank=False)
    discrimination = models.DecimalField(max_digits=20, decimal_places=10, default=0, blank=False)
    difficulty = models.DecimalField(max_digits=20, decimal_places=10, default=0, blank=False)
    timespent = models.DecimalField(max_digits=20, decimal_places=10, default=0, blank=False)
    secid = models.ForeignKey(Section, on_delete=models.CASCADE)
    chid = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = 'STUDENT_EXERCISE'
