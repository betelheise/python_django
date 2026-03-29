from django.db import models

class Flashcard(models.Model):
    # The question on the front
    question = models.CharField(max_length=255)
    # The answer on the back
    answer = models.TextField()
    # A category (e.g., "Math", "Biology")
    topic = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question