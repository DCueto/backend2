from django.contrib import admin
from models import Enlace, Categoria, Agregador

from actions import export_as_csv

# Register your models here.

class EnlaceAdmin(admin.ModelAdmin):
	list_display = ("titulo", "enlace", "categoria", "imagen_voto", "es_popular")
	list_filter = ("categoria", "usuario")
	search_fields = ("categoria__titulo", "usuario__email")
	list_editable = ("enlace", "categoria")
	list_display_links = ("titulo","es_popular")
	actions = [export_as_csv]
	raw_id_fields = ("categoria","usuario")

	def imagen_voto(self, obj):
		url = obj.mis_votos_en_imagen_rosada()
		tag = "<img src='%s'>" % url
		return tag

	imagen_voto.allow_tags = True
	imagen_voto.admin_order_field = "votos"

class EnlaceInline(admin.StackedInline):
	model = Enlace
	extra = 3
	raw_id_fields = ("usuario",)

class CategoriaAdmin(admin.ModelAdmin):
	inlines = [EnlaceInline]

admin.site.register(Agregador)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Enlace, EnlaceAdmin)