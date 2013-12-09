import web
from web import form
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

myform = form.Form(
	form.Textbox('Destination'),
	form.Dropdown('School', schools),
	form.Textarea('Offices'),
	form.Button('Go!', type='submit')
)

class index(object):
    
	def GET(self):
		form = myform()
#		print form.render()
		return render.index(form) #form.render()

	def POST(self):
		form = myform()
		if not form.validates():
			return "failure" #render.formtest(form)
		else:
			return "A page"
			
class routes(object):
	def GET(self):
		pass
	
	def POST(self):
		pass

if __name__ == "__main__":
	web.internalerror = web.debugerror
	app.run()
