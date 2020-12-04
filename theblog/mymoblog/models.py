from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Post(models.Model):
	specie = models.CharField(max_length=255)
	strain = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	information =RichTextField(blank=True, null=True)
	post_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.specie + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('home')
