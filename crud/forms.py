from django import forms

from crud.models import Estudiantes

class EstudianteForm(forms.ModelForm):

	class Meta:
		model = Estudiantes

		fields = [
			'nombre',
			'domicilio',
			'edad',
			'correo',
			'carrera',
			'turno',
		]
		labels = {
			'nombre':'Nombre',
			'domicilio': 'Domicilio',
			'edad': 'Edad',
			'correo': 'Correo',
			'carrera':'Carrera',
			'turno': 'Turno',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'domicilio': forms.TextInput(attrs={'class':'form-control'}),
			'edad': forms.TextInput(attrs={'class':'form-control'}),
			'correo': forms.TextInput(attrs={'class':'form-control'}),
			'carrera': forms.TextInput(attrs={'class':'form-control'}),
			'turno': forms.TextInput(attrs={'class':'form-control'}),
		}