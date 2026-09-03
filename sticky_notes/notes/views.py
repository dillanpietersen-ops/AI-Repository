''' View component - STICKY NOTES APPLICATION
Handles the intercation between the user and application,
managing the presentation logic'''

from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):  # View to display list of all posts
    notes = Note.objects.all()
    context = {"notes": notes,
               "page_title": "List of Notes"}
    return render(request, "notes/note_list.html", context)


def note_detail(request, pk):  # View to display details of specific post
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):  # View to create new post
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):  # View to update existing post
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):  # View to delete existing post
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note_list")
