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
    #setting date to unique, not sure if will raise issue with multiple rounds
    #on the same date, maybe only if two rounds on same course and same date
    date = models.DateField(unique=True)
    strokes = models.IntegerField()
    putts = models.IntegerField()
    fairways_hit = models.IntegerField()
    gir = models.IntegerField()
    
    def __str__(self):
        return str(self.course) + " " + str(self.date)
    
    def print_round(self):
        return [(course, strokes)]
    
    def course_rating(self):
        return self.course.rating
    
    def course_slope(self):
        return self.course.slope
    
    def handicap_diff(self):
        self.differential = ((self.strokes - self.course_rating())*113)/self.course_slope()
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
    
    
