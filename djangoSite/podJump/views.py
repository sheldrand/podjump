from django.shortcuts import render
from podjump.forms import SearchForm
from django.http import HttpResponseRedirect

# Create your views here.
def search_form (request):
    if (request.method == 'POST'):
        form = SearchForm(request.POST)
#        assert False
        if form.is_valid():
            data = form.cleaned_data
            return show_connections (request, data)
    else:
        form = SearchForm()
    return render(request, 'search_form.html',{'form':form})

def show_connections (request):
	#Form passes directly here so we need to check if the data is valid.
	#If not, we send them back to the form page (is this the right way to do it?)
	#places not used in this implementation
	if (request.method == 'POST'):
		form = SearchForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
		else:
			return render(request, 'search_form.html', {'form':form}) #renders search with error message
	else:
		#If it isn't POST, redirect to home form
		return HttpResponseRedirect('/')
	officelist = data.get('offices')
	offices = officelist.split("\n") #splits the offices by newline
	stationnames = []
	for iterator in offices:
		#TODO: strip out u and \r before adding it to list of stations
		stationnames.append(iterator) 
	
	return render(request, 'show.html', {'data':stationnames}) #currently just outputting the data
	


def parceplaces (places):
    #TODO: parse the places passed from the POST call
    pass

