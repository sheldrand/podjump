from django.http import HttpResponse
import datetime

def hello(request):
	return HttpResponse("Please enter your stuff")

def current_time(request):
	now = datetime.datetime.now()
	html="<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)	