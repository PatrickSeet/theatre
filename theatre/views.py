from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
import facebook

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    user_social_auth = request.user.social_auth.filter(provider='facebook').first()
    graph = facebook.GraphAPI(user_social_auth.extra_data['access_token'])
    profile_data = graph.get_object("me")
    picture_data = graph.get_object("me/picture", width=200)
    return render(request, 'profile.html', {'profile': profile_data, 'picture_url': picture_data['url']})