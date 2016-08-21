from django import http
from django import shortcuts

def index(request):
    return shortcuts.render(request, 'policies/life/index.html')

