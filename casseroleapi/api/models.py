from django.db import models

# Models:
class Casserole(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.JSONField(default=dict)
    instructions = models.JSONField(default=dict) 

    def __str__(self):
        return self.name 