from django.shortcuts import render_to_response
import requests


# Create your views here.
def list_users(request):
    response = requests.get("https://api.github.com/users")
    user_data_response = response.json()
    return render_to_response('users/home.html', {
        'list_of_users': user_data_response
    })
