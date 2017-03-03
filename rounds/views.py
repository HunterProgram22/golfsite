from django.shortcuts import render, redirect
from .forms import RoundForm
from django.http.response import HttpResponse
from .forms import Round


def home(request):
    return render(request, 'rounds/home.html', {})

def history(request):
    return render(request, 'rounds/history.html',{})

def round_new(request):
    if request.method == "POST":
        form = RoundForm(request.POST)
        if form.is_valid():
            round = form.save()
            # Add user save at later point here
            round.save()
            return redirect('/')
    else:
        form = RoundForm()
        return render(request, 'rounds/round_edit.html', {'form': form} )


def show(request):
    round_stats = Round.objects.all()
    return render(request, 'rounds/show.html', {'round_stats': round_stats})

def handicap(request):
    round_stats = Round.objects.all()
    round_handicap = []
    for round in round_stats:
        round_handicap.append((round, round.handicap_diff()))
    return render(request, 'rounds/handicap.html', 
                  {'round_handicap': round_handicap})