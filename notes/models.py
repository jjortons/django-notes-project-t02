from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='note_icons/', blank=True, null=True)
    note_date = models.DateField(help_text="Date when note was taken")
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title