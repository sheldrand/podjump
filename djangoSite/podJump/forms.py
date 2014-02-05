from django import forms



class SearchForm(forms.Form):
	SCHOOLS = [
		('Hedion', 'Hedion University'),
		('Amarr Institute', 'Royal Amarr Institute'),
		('Imperial Academy', 'Imperial Academy School'),
		('Republic University', 'Republic University School'),
		('Republic Military School', 'Republic Military School'),
		('Pator Tech School', 'Pator Tech School'),
		('Center for Advanced Studies', 'Center for Advanced Studies'),
		('Federal Navy Academy', 'Federal Navy Academy'),
		('University of Caille School', 'University of Caille School'),
		('School of Applied Knowledge', 'School of Applied Knowledge'),
		('Science & Trade Institute ', 'Science & Trade Institute '),
		('State War Academy', 'State War Academy'),
	]
	destination = forms.CharField(initial='Jita')
	school = forms.ChoiceField(choices=SCHOOLS)
	offices = forms.CharField(widget=forms.Textarea, initial=
    "Please paste your corp office list in to this text box."
    )