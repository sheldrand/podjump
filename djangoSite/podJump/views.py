from django.shortcuts import render

from podjump.forms import SearchForm
from podjump.models import Stastations


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
    officelist = officelist.split("\n")  # splits the offices by newline
    offices = []  # Empty list to contain our cleaned office list
    for i in range(len(officelist)):
        line = officelist[i]
        index = line.rfind(' -')
        if index > 0:
            offices.append(line[:index])
    offices.append(school_stations(data.get('school')))  # Now we add the school stations

    return render(request, 'show.html', {'data': offices})  # currently just outputting the data


def parceplaces(places):
    #TODO: parse the places passed from the POST call
    pass


def school_stations(school):
    #broken
    return "stations"
    schoolstations = []
    stationinfo = Stastations.objects.filter(corproationid_invnames__itemname__icontains=school)
    for station in stationinfo:
        schoolstations.append(station.stationname)
    return schoolstations