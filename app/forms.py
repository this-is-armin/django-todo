from django import forms

from .models import Task


class TaskCreateEditForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['text']
		widgets = {'text':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write your task...'})}
		labels = {'text':''}