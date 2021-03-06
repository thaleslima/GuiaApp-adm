from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core import serializers
from django import forms
from guia.forms import MenuForm
from guia.forms import CityForm
from guia.forms import UserForm
from guia.forms import LocalForm
from guia.models import Menu
from guia.models import City
from guia.models import User
from guia.models import Local
from datetime import date
import json
from django.http import HttpResponse

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






def city_index(request):
	city_list = []
	context = RequestContext(request)
	# if request.method == 'POST':
	city_list = City.objects.all()

	# info = request.GET.get('info')
	return render_to_response('guiaapp/city_index.html', {'list': city_list}, context)


def city_create(request, city_id = 0):
	city = City()

	context = RequestContext(request)
	 
	edit = 'Criar'

	if city_id != 0:
		city = get_object_or_404(City, pk=city_id)
		edit = 'Editar'

	if request.method == 'POST':
		form = CityForm(request.POST, instance=city)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/city')
		else:
			print(form.errors)
	else:
		form = CityForm(instance=city)
	
	return render_to_response('guiaapp/city_create.html', {'form': form, 'edit': edit}, context)



def user_index(request):
	user_list = []
	context = RequestContext(request)
	# if request.method == 'POST':
	user_list = User.objects.all()

	# info = request.GET.get('info')
	return render_to_response('guiaapp/user_index.html', {'list': user_list}, context)


def user_create(request, user_id = 0):
	user = User()

	context = RequestContext(request)
	 
	edit = 'Criar'

	if user_id != 0:
		user = get_object_or_404(User, pk=user_id)
		edit = 'Editar'

	if request.method == 'POST':
		form = UserForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/user')
		else:
			print(form.errors)
	else:
		form = UserForm(instance=user)
	
	return render_to_response('guiaapp/user_create.html', {'form': form, 'edit': edit}, context)


def local_index(request):
	user_list = []
	context = RequestContext(request)
	# if request.method == 'POST':
	local_list = Local.objects.all()

	# info = request.GET.get('info')
	return render_to_response('guiaapp/local_index.html', {'list': local_list}, context)


def local_create(request, local_id = 0):
	local = Local()

	context = RequestContext(request)
	 
	edit = 'Criar'

	if local_id != 0:
		local = get_object_or_404(Local, pk=local_id)
		edit = 'Editar'

	if request.method == 'POST':
		local.date = date.today()
		form = LocalForm(request.POST, instance=local)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/local')
		else:
			print(form.errors)
	else:
		form = LocalForm(instance=local)
	
	return render_to_response('guiaapp/local_create.html', {'form': form, 'edit': edit}, context)


def get_locals(request):
    # contatos = Local.objects.all()
    # retorno = serializers.serialize("json",  contatos)
    # return HttpResponse(retorno, content_type='application/json')
    data = {}
    data['something'] = 'useful'
    return HttpResponse(json.dumps(data), content_type = "application/json")


def login_user(request, login, password):
	if request.method == 'GET':
		if login == "admin" and password == "123":
			data = {}
			data['id'] = 1
			data['name'] = "Admin"
			data['email'] = "admin@admin.com"
			data['login'] = login
			return HttpResponse(json.dumps(data), content_type = "application/json")

	data = {}
	
	data['status'] = "Fail"
	data['message'] = "Usuario nao cadastrado."
	return HttpResponse(json.dumps(data), content_type = "application/json; charset=utf-8")

def get_products(request):

	categories = []

	category = {}
	category['id'] = 1
	category['name'] = "Bebidas"

	products = []
	product = {}
	product['id'] = 1
	product['name'] = "Coca Cola lata"
	product['price'] = 3.20
	products.append(product)

	product = {}
	product['id'] = 2
	product['name'] = "Fanta lata"
	product['price'] = 1.30
	products.append(product)

	product = {}
	product['id'] = 3
	product['name'] = "Antarctica lata"
	product['price'] = 4.20
	products.append(product)

	product = {}
	product['id'] = 4
	product['name'] = "Skol lata 300 ml"
	product['price'] = 6.20
	products.append(product)

	product = {}
	product['id'] = 5
	product['name'] = "Skol garrafa 600 ml"
	product['price'] = 8.20
	products.append(product)

	category['products'] = products
	categories.append(category)



	category = {}
	category['id'] = 2
	category['name'] = "Pratos"

	products = []
	product = {}
	product['id'] = 6
	product['name'] = "Maminha"
	product['price'] = 9.90
	products.append(product)

	product = {}
	product['id'] = 7
	product['name'] = "Alcatra"
	product['price'] = 5.10
	products.append(product)

	product = {}
	product['id'] = 8
	product['name'] = "Coxao"
	product['price'] = 4.10
	products.append(product)

	product = {}
	product['id'] = 9
	product['name'] = "Bisteca Suina"
	product['price'] = 9.10
	products.append(product)

	product = {}
	product['id'] = 10
	product['name'] = "File de frango"
	product['price'] = 8.10
	products.append(product)

	category['products'] = products
	categories.append(category)


	category = {}
	category['id'] = 3
	category['name'] = "Pizzas"

	products = []
	product = {}
	product['id'] = 11
	product['name'] = "Muzzarela"
	product['price'] = 1.20
	products.append(product)

	products = []
	product = {}
	product['id'] = 12
	product['name'] = "Marquerita"
	product['price'] = 1.50
	products.append(product)

	products = []
	product = {}
	product['id'] = 13
	product['name'] = "Provolone"
	product['price'] = 12.40
	products.append(product)

	products = []
	product = {}
	product['id'] = 13
	product['name'] = "Lombinho"
	product['price'] = 32.40
	products.append(product)

	products = []
	product = {}
	product['id'] = 13
	product['name'] = "Portuguesa"
	product['price'] = 13.40
	products.append(product)
	category['products'] = products
	categories.append(category)
	return HttpResponse(json.dumps(categories), content_type = "application/json; charset=utf-8")

def get_commands(request):
	commands = []


	for x in range(1, 30):
		command = {}
		command['id'] = x
		command['name'] = format(x, '02d')

		command['status'] = 1

		if x == 3 or x == 7 or x == 21 or x == 6:
			command['status'] = 2

		commands.append(command)

	return HttpResponse(json.dumps(commands), content_type = "application/json; charset=utf-8")


