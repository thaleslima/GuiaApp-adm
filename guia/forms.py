from django import forms
from guia.models import Menu
from guia.models import City
from guia.models import Local

class MenuForm(forms.ModelForm):
	# description = forms.CharField(widget=forms.TextInput(attrs={'class': 'special', 'type' : 'email'}))
	
	id = forms.CharField(required=False, widget=forms.HiddenInput())

	description = forms.CharField()
	description.widget.attrs['class'] = 'form-control'
	description.widget.attrs['required'] = ''
	

	active = forms.BooleanField(initial=False, required=False)
	
	class Meta:
		model = Menu
		fields = ('id', 'description', 'active')



class CityForm(forms.ModelForm):
	# description = forms.CharField(widget=forms.TextInput(attrs={'class': 'special', 'type' : 'email'}))
	
	id = forms.CharField(required=False, widget=forms.HiddenInput())

	description = forms.CharField()
	description.widget.attrs['class'] = 'form-control'
	description.widget.attrs['required'] = ''
	
	uf = forms.CharField()
	uf.widget.attrs['class'] = 'form-control'
	uf.widget.attrs['required'] = ''

	
	class Meta:
		model = Menu
		fields = ('id', 'description', 'uf')


class UserForm(forms.ModelForm):
	# description = forms.CharField(widget=forms.TextInput(attrs={'class': 'special', 'type' : 'email'}))
	
	id = forms.CharField(required=False, widget=forms.HiddenInput())

	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'email', 'required' : ''}))
	password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'password', 'required' : ''}))
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'text', 'required' : ''}))
	lastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'text'}))
		
		
	class Meta:
		model = Menu
		fields = ('id', 'email', 'password', 'name', 'lastName')


class LocalForm(forms.ModelForm):
	id = forms.CharField(required=False, widget=forms.HiddenInput())

	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'text', 'required' : ''}))
	telephone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'text'}))
	site = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'text'}))
	email = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'email'}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'cols' : '20', 'rows' : '12'}))
	address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'text'}))
	latitude = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'text'}))
	longitude = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'text'}))
	active = forms.BooleanField(initial=False, required=False)
	pathImage = forms.CharField(required=False, widget=forms.HiddenInput())
	city = forms.ModelChoiceField(queryset=City.objects.all(), required=False, widget=forms.Select(attrs={'class':'form-control', 'required' : ''}))
	menu = forms.ModelChoiceField(queryset=Menu.objects.all(), required=False, widget=forms.Select(attrs={'class':'form-control', 'required' : ''}))
	
	class Meta:
		model = Local
		fields = ('id', 'name', 'telephone', 'site', 'email', 'description', 'address', 'latitude', 'longitude', 'active', 'pathImage', 'city', 'menu' )
