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

def show_connections (request, places):
    assert False