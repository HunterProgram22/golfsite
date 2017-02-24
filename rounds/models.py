from django.db import models

class Course(models.Model):
    course = models.CharField(max_length=200, unique=True)
    rating = models.IntegerField()
    slope = models.IntegerField()
    par = models.IntegerField()
    
    def __str__(self):
        return self.course
    
class Round(models.Model):
    course = models.ForeignKey(Course, to_field="course")
    date = models.DateField()
    strokes = models.IntegerField()
    putts = models.IntegerField()
    fairways_hit = models.IntegerField()
    gir = models.IntegerField()
    
    def __str__(self):
        return str(self.course) + " " + str(self.date)
    
    
