from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.contrib import auth
from django.template.context_processors import csrf
import random

from football.models import Cup, Referee, Team, Lists, ArchiveGame


def start(request):
    context = {'username': auth.get_user(request).username}
    return render_to_response('football/start.html', context)

def tournaments(request):
    context = {}
    context["tournaments"] = Cup.objects.all()
    return render_to_response("football/tournaments.html", context)

def tournament(request, tournament_id):
    context = {"cup" : Cup.objects.get(id=tournament_id), "referee" : Cup.objects.get(id=tournament_id).referee}
    return render_to_response("football/tournament.html", context)

def info(request):
    context = {'username': auth.get_user(request).username}
    return render_to_response('football/info.html', context)

def registration(request, tournament_id):
    context = {}
    context.update(csrf(request))
    if request.POST:
        team = request.POST.get("team")
        number = request.POST.get("number")
        captain = request.POST.get("captain")
        if number and team and captain:
            if number.isdigit():  # поле "кол-во игроков" не может быть ничем кроме цифры
                if Team.objects.filter(team_name=team).exists():
                    t = Team.objects.get(team_name=team)
                    if t.number_of_players != number or t.team_captain != captain: #кол-во игроков и капитан у команды может меняться, но команда та же
                        t.number_of_players = number
                        t.team_captain = captain
                        t.save()
                    if Lists.objects.filter(team=t, cup=Cup.objects.get(id=tournament_id)).exists():
                        context["team_error"] = "Данная команда уже зарегестрировалась на этот турнир!"
                    else:
                        l = Lists(team=t, cup=Cup.objects.get(id=tournament_id))
                        l.save()
                        if Lists.objects.filter(cup=Cup.objects.get(id=tournament_id)).count() == Cup.objects.get(id=tournament_id).count_commands:
                            play_game_method(tournament_id)
                else:
                    t = Team(team_name=team, number_of_players=number, team_captain=captain)
                    t.save()
                    l = Lists(team=t, cup=Cup.objects.get(id=tournament_id))
                    l.save()
                    return render_to_response('football/tournaments.html')

        else:
            context["team_error"] = "Заполенены не все поля необходимые для регистрации команды!"
            context["cup"] = Cup.objects.get(id=tournament_id)
            return render_to_response('football/registration_to_cup.html', context)
    context["cup"]= Cup.objects.get(id=tournament_id)
    return render_to_response('football/registration_to_cup.html', context)

def play_game_method(chemp):
    listik = Lists.objects.filter(cup=chemp)
    if listik.__len__() != 1:
        game(listik, chemp, int(listik.__len__()/2))


def game(list, cup, tour):
    store = []
    match = {}
    for i in range(len(list)):
        if i%2 == 1:
            continue
        match[list[i]] = random.randint(0,5)
        match[list[i+1]] = random.randint(0,5)
        if match[list[i]] == match[list[i+1]]:
            if random.randint(0, 1):
                match[list[i]] += 1
            else:
                match[list[i+1]] += 1
        if match[list[i]] > match[list[i+1]]:
            store.append(list[i])
        else:
            store.append(list[i+1])
        print(type(match[list[i]]))

        ar  = ArchiveGame(tourney=Cup.objects.get(id=cup), team_first=list[i].team, team_second=list[i+1].team,
                          goal_first=match[list[i]], goal_second=match[list[i + 1]], tour=tour)
        ar.save()
    return store


    
