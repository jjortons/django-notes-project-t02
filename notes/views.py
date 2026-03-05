from django.shortcuts import render
from .models import Note

def note_list(request):
    # Fetch all notes, ordered by the date they were taken
    notes = Note.objects.all().order_by('-note_date')
    return render(request, 'notes/index.html', {'notes': notes})