import web
import dbRead

urls = (
  '/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

schools = [
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
	('State War Academy', 'State War Academy')
]



class index(object):
    def GET(self):
#		form = web.input(name="Nobody")
#		greeting = "Hello %s" % form.name
		
		form = web.form.Dropdown('Schools', schools)
		print form
		return form


if __name__ == "__main__":
    app.run()