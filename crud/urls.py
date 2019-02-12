from django.conf.urls import url, include
from crud.views import home, estudiante_edit, estudiante_view, estudiante_delete
#estudiante_view, estudiante_edit


urlpatterns = [
	url(r'^nuevo$', estudiante_view, name='estudiante_crear'),
	url(r'^editar/([0-9]+)/$', estudiante_edit, name='estudiante_editar'),
	url(r'^eliminar/([0-9]+)/$',estudiante_delete, name='estudiante_eliminar'),
]