from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from . import models
from . import forms


class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/list.html'


class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')