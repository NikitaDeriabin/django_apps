from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myView(request):
    visited = request.session.get('visited', 0) + 1
    request.session['visited'] = visited
    if visited > 4:
        del(request.session['visited'])
    resp = HttpResponse('view count' + '=' + str(visited))
    resp.set_cookie('dj4e_cookie', '8807b219', max_age=1000)
    return resp
