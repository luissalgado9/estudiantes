# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from crud.models import Estudiantes
from crud.forms import EstudianteForm
from django.http import HttpResponse

# Create your views here.


def home(request):
	alumnos = Estudiantes.objects.all()
	contexto = {'estudiantes':alumnos}
	return render(request,'home.html', {'estudiantes':alumnos,'title':'Lista de estudiantes'})

def estudiante_view(request):
	if request.method == 'POST':
		form = EstudianteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	else:
		form = EstudianteForm()
	return render(request, 'agregar_form.html', {'form':form,'title':'Agregar Estudiante'})

def estudiante_edit(request,id_estudiante):
	estudiante = Estudiantes.objects.get(id=id_estudiante)
	if request.method == 'GET':
		form = EstudianteForm(instance=estudiante)
	else:
		form = EstudianteForm(request.POST,instance=estudiante)
		if form.is_valid():
			form.save()
			return redirect('index')
	return render(request,'agregar_form.html', {'form':form,'title':'Editar Alumno'})

def estudiante_delete(request,id_estudiante):
	estudiante = Estudiantes.objects.get(id=id_estudiante)
	if request.method == 'POST':
		estudiante.delete()
		return redirect('index')
	return render(request,'eliminar_form.html', {'estudiante':estudiante,'title':'Eliminar estudiante'})


















