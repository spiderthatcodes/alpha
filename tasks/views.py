from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm


@login_required(login_url='/accounts/login/')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(False)
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form
    }

    return render(request, "tasks/create.html", context)
