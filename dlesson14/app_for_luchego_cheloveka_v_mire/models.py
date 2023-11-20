from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    quantity_of_likes = models.PositiveIntegerField()


    def __str__(self):
        return self.name