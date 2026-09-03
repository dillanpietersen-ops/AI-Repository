'''Model component represents business logic and data structure'''

from django.db import models


class Note(models.Model):  # Model representing a sticky note post
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Define foreign key
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title


class Author(models.Model):  # Model representing the author of a Sticky Note
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
