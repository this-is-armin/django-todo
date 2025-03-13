from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from .models import Task 
from .forms import TaskCreateEditForm


class TasksView(View):
	template_name = 'task/tasks.html'
	form_class = TaskCreateEditForm

	def get(self, request):
		tasks = Task.objects.all()
		form = self.form_class()
		return render(request, self.template_name, {'tasks':tasks, 'form':form})

	def post(self, request):
		tasks = Task.objects.all()
		form = self.form_class(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, 'The task was created', 'success')
			return redirect('app:tasks')
		return render(request, self.template_name, {'tasks':tasks, 'form':form})


def task_delete_view(request, **kwargs):
	task = Task.objects.filter(pk=kwargs['pk'])	
	if task.exists():
		task.delete()
		messages.success(request, 'The task was deleted', 'success')
	return redirect('app:tasks')


class TaskEditView(View):
	template_name = 'task/edit.html'
	form_class = TaskCreateEditForm

	def setup(self, request, *args, **kwargs):
		self.task_instance = get_object_or_404(Task, pk=kwargs['pk'])
		return super().setup(request, *args, **kwargs)

	def dispatch(self, request, *args, **kwargs):
		if self.task_instance.finished == True: return redirect('app:tasks')
		return super().dispatch(request, *args, **kwargs)

	def get(self, request, **kwargs):
		task = self.task_instance
		form = self.form_class(instance=task)
		return render(request, self.template_name, {'form':form})

	def post(self, request, **kwargs):
		task = get_object_or_404(Task, pk=kwargs['pk'])
		form = self.form_class(request.POST, instance=task)

		if form.is_valid():
			form.save()
			messages.success(request, 'The task was edited', 'success')
			return redirect('app:tasks')
		return render(request, self.template_name, {'form':form})


def task_finish_view(request, **kwargs):
	task = get_object_or_404(Task, pk=kwargs['pk'])
	if task.finished == False:
		task.finished = True
		task.save()
		messages.success(request, 'The task was finished', 'success')
	return redirect('app:tasks')