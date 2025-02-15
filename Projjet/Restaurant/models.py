from django.db import models

# Create your models here.
class Menu(models.Model):
	nom = models.CharField(max_length=100)
	description = models.TextField()
	disponible = models.BooleanField(default=True)

	def __str__(self):
		return self.nom
