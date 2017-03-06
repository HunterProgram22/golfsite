from django.db import models

class Course(models.Model):
    course = models.CharField(max_length=200, unique=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    slope = models.IntegerField()
    par = models.IntegerField()
    
    def __str__(self):
        return self.course
    
class Round(models.Model):
    course = models.ForeignKey(Course, to_field="course")
    #setting date to unique, not sure if will raise issue with multiple rounds
    #on the same date, maybe only if two rounds on same course and same date
    date = models.DateField(unique=True)
    strokes = models.IntegerField()
    putts = models.IntegerField()
    fairways_hit = models.IntegerField()
    gir = models.IntegerField()
    equistrokes = models.IntegerField()
    
    def __str__(self):
        return str(self.date) + " " + str(self.course) 
    
    def print_round(self):
        return [(course, strokes)]
    
    def course_rating(self):
        self.course.rating = float(self.course.rating)
        return self.course.rating
    
    def course_slope(self):
        self.course.slope = float(self.course.slope)
        return self.course.slope
    
    def handicap_diff(self):
        self.differential = ((self.equistrokes - self.course_rating())*113)/self.course_slope()
        self.differential = round(self.differential, 1)
        return self.differential
    
class Shots(models.Model):
    date = models.OneToOneField(Round, to_field="date")
    drdist = models.IntegerField()
    dracc = models.IntegerField()
    par3tee = models.IntegerField()
    lngdist = models.IntegerField()
    lngacc = models.IntegerField()
    shtdist = models.IntegerField()
    shtacc = models.IntegerField()
    pitch = models.IntegerField()
    chip = models.IntegerField()
    putt = models.IntegerField()
    penal = models.IntegerField()
    coursemgmt = models.IntegerField()
    
    
