from random import choice

frases = ["leonidas esta sentado", "freddy se fue", "Hackintosh mola", "Frontend Dev", "Yeah!!!!"]

def ejemplo(request):
	return {"frase" : choice(frases)}