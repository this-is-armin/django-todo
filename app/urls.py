from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
	path('', views.TasksView.as_view(), name='tasks'),
	path('<pk>/delete/', views.task_delete_view, name='task_delete'),
	path('<pk>/edit/', views.TaskEditView.as_view(), name='task_edit'),
	path('<pk>/finish/', views.task_finish_view, name='task_finish')
]