from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from models import *
from django.shortcuts import get_object_or_404
from forms import *
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.order_by("-votos").all()
	template = "index.html"

	return render_to_response(template, locals())

def categoria(request, id_categoria):
	categorias = Categoria.objects.all()
	cat = get_object_or_404(Categoria, pk = id_categoria)
	# cat = Categoria.objects.get(pk = id_categoria)
	enlaces = Enlace.objects.filter(categoria = cat)
	template = "index.html"

	return render_to_response(template, locals())


def minus(request, id_enlace):
	enlace = Enlace.objects.get(pk=id_enlace)
	enlace.votos = enlace.votos - 1
	enlace.save()
	return HttpResponseRedirect("/")
@login_required

def plus(request, id_enlace):
	enlace = Enlace.objects.get(pk=id_enlace)
	enlace.votos = enlace.votos + 1
	enlace.save()
	return HttpResponseRedirect("/")
@login_required

def add(request):
	categorias = Categoria.objects.all()
	if request.method == "POST":
		form = EnlaceForm(request.POST)
		if form.is_valid():
			enlace = form.save(commit = False)
			enlace.usuario = request.user
			enlace.save()
			return HttpResponseRedirect("/")
	else:
		form = EnlaceForm()

	template = "form.html"
	return render_to_response(template, context_instance = RequestContext(request,locals()))
@login_required

def hora_actual(request):

	""" MODO LARGO
	ahora = datetime.now
	t = get_template("hora.html")
	c = Context({"hora": ahora, "usuario":"Dani"})
	html = t.render(c)
	return HttpResponse(html) """

	now = datetime.now()
	return render_to_response("hora.html",{"hora" : now, "usuario" : "Dani"})
