from django import forms
from guia.models import Menu

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