from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime

# Create your views here.

def hora_actual(request):

	""" MODO LARGO
	ahora = datetime.now
	t = get_template("hora.html")
	c = Context({"hora": ahora, "usuario":"Dani"})
	html = t.render(c)
	return HttpResponse(html) """

	now = datetime.now()
	return render_to_response("hora.html",{"hora" : now, "usuario" : "Dani"})
