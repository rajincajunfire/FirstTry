from django.shortcuts import render
from .models import Person

def home(request):
	name = "Oluwakemi Oso"
	return render(request, 'home.html', {'name':name})

def about(request):
	name = "Oluwakemi Oso"
	aboutText = "This is more information about Oluwakemi Oso"
	age = 20
	birthday = "December 25th, 1991"
	hometown = "Phoenix, Arizona"
	bio = """
	I recently graduated from the University of Arizona, where I was politically active 
	as Student Director of an internship program, FORCE (Feminists Organized to Resist, 
	Create, and Empower). In May 2014, I moved to Washington, DC to begin fighting for 
	reproductive justice for Unite for Reproductive and Gender Equity as the Southern Field 
 	Associate to help college students organize for change in their communities. Like most 
	millennials, I have been surrounded by computers and technology since birth. Learning 
	to program piqued my interest for years, and Code for Progress presented itself as the 
	perfect opportunity to develop those skills and use them for the greater good. I am 
	committed to creating an app that allows local neighborhoods to crowd-source physical 
	resource. Similar to apps like Kickstarter or Indiegogo, this will allow for community-created 
	projects such as neighborhood beautification, safety kits for homeless individuals, or stocking 
	a local food kitchen. I want community members to not just contribute, but also feel empowered 
	to spearhead the change they want to see.
	"""
	
	context = {'name':name, 
				'aboutText':aboutText, 
				'age':age, 
				'birthday':birthday, 
				'hometown':hometown, 
				'bio':bio}

	return render(request, 'about.html', context)

def whatever(request):
	name = "Kemi"
	age = 20
	birthday = "Christmas"
	return render(request, 'whatever.html', {'name':name, 'age':age, 'birthday':birthday})

def family(request):
	personAdd = Person.objects.create(first_name='Obafemi', last_name='Oso', age=24, about_me = "The oldest child")
	personAdd.save()
	familyList = Person.objects.all()









	return render(request, 'family.html', context)