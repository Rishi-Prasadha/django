from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Todo
from .forms import TodoForm

# Create your views here.

def index(request):
	items = Todo.objects.order_by('-date')
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo')
	form= TodoForm()

	page = {
		"forms": form,
		"list": items,
		"title": "TODO LIST",
	}

	return render(request, 'todo/index.html', page)

def remove(request, item_id):
	target = Todo.objects.get(id=item_id)
	target.delete()

	messages.info(request, 'item removed!')

	return redirect('todo')