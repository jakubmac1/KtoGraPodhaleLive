# matches/admin.py
from django.contrib import admin
from .models import Division, Team, Match

admin.site.register(Division)
admin.site.register(Team)
admin.site.register(Match)
