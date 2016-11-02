from django.http import HttpResponse

def index(request):

	return HttpResponse("<h1>This is the Music app homepage</h1>")