from django.db import models

class AlgSet(models.Model):
    name = models.CharField(max_length=100) # e.g. "CLL"
    description = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='set_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Flashcard(models.Model):
    name = models.CharField(max_length=100, default="Unnamed Case")

    alg_set = models.ForeignKey(AlgSet, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    image = models.ImageField(upload_to='cube_cases/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.anme
