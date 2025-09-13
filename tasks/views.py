from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by("is_completed", "due_date")


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "due_date", "priority"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:index")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description", "due_date", "priority", "is_completed"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:index")

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:index")

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.is_completed = True
    task.save()
    return redirect("tasks:index")
