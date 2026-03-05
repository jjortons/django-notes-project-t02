from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # This makes the admin list look professional
    list_display = ('title', 'category', 'note_date', 'date_add')
    list_filter = ('category', 'note_date')
    search_fields = ('title', 'content')