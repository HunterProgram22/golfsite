from django.shortcuts import render, redirect
from .forms import RoundForm


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

  