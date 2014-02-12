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
			assert False
			data = form.cleaned_data
		else:
			return HttpResponseRedirect('/') #should send home
#	stations = parceplaces(data)
	return render(request, 'show.html')
	


def parceplaces (places):
    #TODO: parse the places passed from the POST call
    pass

