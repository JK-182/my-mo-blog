from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('specie', 'strain', 'author', 'information')

		widgets = {
			'specie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Microorganism Specie'}),
			'strain': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Microorganism Strain'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type':'hidden'}),
			'information': forms.Textarea(attrs={'class': 'form-control'}),

		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('specie', 'strain', 'information')

		widgets = {
			'specie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Microorganism Specie'}),
			'strain': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Microorganism Strain'}),
			'information': forms.Textarea(attrs={'class': 'form-control'}),

		}