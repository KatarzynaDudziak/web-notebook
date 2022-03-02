from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import *
from .forms import *
from users import *

@login_required(login_url='/users/login')
def index(request):
    notes = NoteModel.objects.all().order_by('-date')

    if request.user.username != 'admin':
        notes = notes.filter(author=request.user)

    return render(request, 'index.html', {"notes": notes})

@login_required(login_url='/users/login')
def form(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            note = NoteModel(title=title, content=content, date=timezone.now(), author=request.user)
            note.save()
            return HttpResponseRedirect('/noteapp/')

    return render(request, 'form.html')

@login_required(login_url='/users/login')
def edit(request, id):
    try:
        note = NoteModel.objects.get(id = id)
    except NoteModel.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            newNote = NoteModel.objects.get(id = id)
            newNote.title = form.cleaned_data['title']
            newNote.content = form.cleaned_data['content']
            newNote.date = timezone.now()
            newNote.save()
            return HttpResponseRedirect('/noteapp/')
    
    return render(request, 'edit.html', {"note" : note})

@login_required(login_url='/users/login')
def delete(request):
    if request.method == 'POST':
        try:
            NoteModel.objects.get(id = request.POST['id']).delete()
        except:
            return handle_not_found(request, exception=None)

    return HttpResponseRedirect('/noteapp/')

@login_required(login_url='/users/login')
def note(request, id):
    note = NoteModel.objects.get(id = id)
    
    return render(request, 'note.html', {"note" : note})
    
@login_required(login_url='/users/login')
def handle_not_found(request, exception):
    return render(request, 'not_found.html')
