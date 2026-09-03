# ADMIN RESGITRATION PROGRAM FOR STICKY NOTES APP
# notes/admin.py
from django.contrib import admin
from .models import Note, Author


# sticky Notes Note Admin Registration
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "content")


# Sticky Notes Author Admin Registration
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
