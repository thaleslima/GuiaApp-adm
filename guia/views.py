from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from guia.forms import MenuForm
from guia.models import Menu

def menu_index(request):
	menu_list = []
	context = RequestContext(request)
	# if request.method == 'POST':
	menu_list = Menu.objects.all()

	# info = request.GET.get('info')
	return render_to_response('guiaapp/menu_index.html', {'menu_list': menu_list}, context)

def menu_create(request, menu_id = 0):
	menu = Menu()

	context = RequestContext(request)
	 
	edit = 'Criar'

	if menu_id != 0:
		menu = get_object_or_404(Menu, pk=menu_id)
		edit = 'Editar'

	if request.method == 'POST':
		form = MenuForm(request.POST, instance=menu)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/menu')
		else:
			print(form.errors)
	else:
		form = MenuForm(instance=menu)
	
	return render_to_response('guiaapp/menu_create.html', {'form': form, 'edit': edit}, context)


def menu_delete(request, menu_id):
	menu = Menu()
	context = RequestContext(request)
	menu = get_object_or_404(Menu, pk=menu_id)

	if request.method == 'POST':
		menu.delete()
		return HttpResponseRedirect('/menu/')
	
	return render_to_response('guiaapp/menu_delete.html', {'menu': menu }, context)
