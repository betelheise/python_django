from django.db import models

class Flashcard(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    topic = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='cube_cases/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
