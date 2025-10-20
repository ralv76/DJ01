from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

def films_list(request):
	films = Film.objects.all()
	return render(request, 'films/films_list.html', {'films': films})

def add_film(request):
	error = ""
	if request.method == 'POST':
		form = FilmForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('films_list')
		else:
			error = "Данные были заполнены некорректно"
	else:
		form = FilmForm()
	return render(request, 'films/add_film.html', {'form': form, 'error': error})
