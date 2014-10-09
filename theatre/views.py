from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
import facebook
from theatre.models import Showtime
from theatre.models import Movie

# Create your views here.
def home(request):
    return render(request, 'home.html')

def seat_test(request):

    return render(request, 'seat_test.html')
@csrf_exempt
def stripe(request):

    return render(request, 'stripe.html')

@csrf_exempt
@login_required()
def movie(request):

    user_social_auth = request.user.social_auth.filter(provider='facebook').first()
    graph = facebook.GraphAPI(user_social_auth.extra_data['access_token'])
    profile_data = graph.get_object("me")
    picture_data = graph.get_object("me/picture")

    return render(request, 'movies.html', {'profile': profile_data, 'picture_url': picture_data['url']})

@csrf_exempt
@login_required()
def showtime(request):
    return render(request, 'showtime.html')

@csrf_exempt
@login_required()
def get_time(request, movieID):

    show_times = Showtime.objects.filter(movie_id=movieID)

    json_res = []

    for show_time in show_times:
        json_res.append({
            'time': show_time.time,
        })

    return HttpResponse(json.dumps(json_res),content_type='application/json')

@csrf_exempt
@login_required()
def api_movie(request):

    all_movies = Movie.objects.all()

    json_res = []

    for movie in all_movies:
        json_res.append({
            'id': movie.id,
            'name': movie.name,
            'director': movie.director,
        })

    return HttpResponse(json.dumps(json_res),content_type='application/json')