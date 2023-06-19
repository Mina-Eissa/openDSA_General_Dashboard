from django.db import models
from .instructor import Instructor
from .book import Book

class InstructorBook(models.Model):
    instid = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = 'INSTRUCTOR_BOOK'
