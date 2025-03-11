from django.db import models
from django.urls import reverse


class Task(models.Model):
	text = models.CharField(max_length=200)
	finished = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.text

	def task_delete(self):
		return reverse('app:task_delete', args=[self.pk])

	def task_edit(self):
		return reverse('app:task_edit', args=[self.pk])

	def task_finish(self):
		return reverse('app:task_finish', args=[self.pk])