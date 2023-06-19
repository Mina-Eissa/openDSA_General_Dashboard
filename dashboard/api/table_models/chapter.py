from django.db import models
from .book import Book

class Chapter(models.Model):
    chid = models.AutoField(primary_key=True)
    chname = models.CharField(max_length=100, default='', blank=False)
    number_of_sections = models.IntegerField(default=0, blank=False)
    number_of_exercises = models.IntegerField(default=0, blank=False)
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = 'CHAPTER'
