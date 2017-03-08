from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .forms import RoundForm, CourseForm, ShotsForm
from .models import Round, Shots
from .functions import calcHandicap, yearAverages

def home(request):
    year_stats = []
    # TODO Filter all round objects and get years and set range at low and high+1
    for year in range(2016, 2018):
        year_rounds = Round.objects.filter(date__year=year)
        year_stats.append(yearAverages(year_rounds))
    return render(request, 'rounds/home.html', {'year_stats': year_stats})

def manage(request):
    return render(request, 'rounds/manage.html',{})

def round_new(request):
    if request.method == "POST":
        form = RoundForm(request.POST)
        if form.is_valid():
            round = form.save()
            # Add user save at later point here
            round.save()
            return redirect('/manage/')
    else:
        form = RoundForm()
        return render(request, 'rounds/round_edit.html', {'form': form} )
    
def delete_round(request):
    if request.method == 'POST':
        id = int(request.path.replace("/delete_round/", ""))
        round = Round.objects.get(pk=id)
        round.delete()
        return redirect('/show/')
    else:
        return HttpResponse("Did not post")

    
def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            # Add user save at later point here
            course.save()
            return redirect('/')
    else:
        form = CourseForm()
        return render(request, 'rounds/course_edit.html', {'form': form})
    
def shots_new(request):
    if request.method == "POST":
        form = ShotsForm(request.POST)
        if form.is_valid():
            shots = form.save()
            # Add user save at later point here
            shots.save()
            return redirect('/')
    else:
        form = ShotsForm()
        return render(request, 'rounds/shots_edit.html', {'form': form})


def show(request):
        round_stats = Round.objects.all().order_by('-date')
        return render(request, 'rounds/show.html', {'round_stats': round_stats})

def handicap(request):
    round_stats = Round.objects.all().order_by('date')
    round_handicap = []
    diffList = []
    handicapTotal = 0 
    round_count = 0
    for round in round_stats:
        round_count += 1
        diffList.append(round.handicap_diff())
        handicapTotal = calcHandicap((round_count), diffList)
        round_handicap.append((round, round.handicap_diff(), handicapTotal))
    return render(request, 'rounds/handicap.html', 
                  {'round_handicap': round_handicap})


def sop(request):
    sop_stats = Shots.objects.all()
    return render(request, 'rounds/sop.html', {'sop_stats': sop_stats})