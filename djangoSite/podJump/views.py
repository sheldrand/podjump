from django.shortcuts import render

from podjump.forms import SearchForm


# Create your views here.


def search_form(request):
    #I'm not sure if this function is truly needed
    if request.method == 'POST':
        form = SearchForm(request.POST)
        #        assert False
        if form.is_valid():
            data = form.cleaned_data
            return show_connections(request)
    else:
        form = SearchForm()
    return render(request, 'search_form.html', {'form': form})


def show_connections(request):
    #Form passes directly here so we need to check if the data is valid.
    #If not, we send them back to the form page (is this the right way to do it?)
    #places not used in this implementation
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        else:
            return render(request, 'search_form.html', {'form': form})  # renders search with error message
    destination = data.get('destination')
    officelist = data.get('offices')
    offices = officelist.split("\n")  # splits the offices by newline
    offices = [i.rstrip('\r') for i in offices]  # strips out the \r at the end of each line (wait, why do I care?)

    return render(request, 'show.html', {'data': offices})  # currently just outputting the data


def parceplaces(places):
    #TODO: parse the places passed from the POST call
    pass

