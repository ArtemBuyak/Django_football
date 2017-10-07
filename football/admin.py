from django.contrib import admin

from .models import Cup, Team, Referee, Lists, ArchiveGame

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name of the team', {'fields': ['team_name']}),
        ('Number of players', {'fields': ['number_of_players']}),
        ('Captain\'s name', {'fields': ['team_captain']}),
]

admin.site.register(Team, TeamAdmin)

class CupAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['date']}),
        ('Cup Name', {'fields': ['cup_name']}),
        ('About cup', {'fields': ['cup_information']}),
        ('Number of teams', {'fields': ['count_commands']}),
        ('Prize', {'fields': ['prize']}),
        ('Referee', {'fields': ['referee']})
    ]

admin.site.register(Cup, CupAdmin)
admin.site.register(Referee)
admin.site.register(Lists)
admin.site.register(ArchiveGame)