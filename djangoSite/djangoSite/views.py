from django.http import HttpResponse
import datetime

def hello(request):
	return HttpResponse("Please enter your stuff")

def current_time(request):
	now = datetime.datetime.now()
	html="<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def hour_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html="<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse (html)