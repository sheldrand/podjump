from django.http import HttpResponse
import datetime

def current_time(request):
	now = date.datetime.now()
	htlp="<html><body><It is now %s.</body></html>" % now
	return Httpresponse(html)