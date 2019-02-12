# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Estudiantes(models.Model):
	nombre = models.CharField(max_length=30)
	domicilio = models.CharField(max_length=50)
	edad = models.CharField(max_length=2)
	correo = models.EmailField(max_length=30)
	carrera = models.CharField(max_length=30)
	turno = models.CharField(max_length=20)
