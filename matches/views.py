# matches/views.py

from django.shortcuts import render
from django.utils import timezone
from .models import Match, Division
from datetime import timedelta, datetime

def get_current_week():
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week

def home(request):
    start_of_week, end_of_week = get_current_week()
    divisions = Division.objects.all()
    matches_by_division = {}
    for division in divisions:
        matches = Match.objects.filter(
            home__division=division,
            time__date__range=[start_of_week, end_of_week]
        ).order_by('time')
        if matches.exists():
            matches_by_division[division] = matches
    return render(request, 'matches/home.html', {'matches_by_division': matches_by_division})
