# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from crud.models import Estudiantes
# Register your models here.

class TablaEstudiante(admin.ModelAdmin):
	list_display = ('nombre', 'domicilio', 'edad', 'correo', 'carrera','turno','foto')

admin.site.register(Estudiantes, TablaEstudiante)


