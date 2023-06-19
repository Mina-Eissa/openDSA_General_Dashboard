from django.db import models

class Book(models.Model):
    bookid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=100, default='', blank=False)
    number_of_chapters = models.IntegerField(default=0, blank=False)
    number_of_exercises = models.IntegerField(default=0, blank=False)
    
    class Meta:
        managed = True
        db_table = 'BOOK'
