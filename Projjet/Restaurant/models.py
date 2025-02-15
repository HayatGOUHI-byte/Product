from django.db import models

# Create your models here.
class Menu(models.Model):
	nom = models.CharField(max_length=100)
	description = models.TextField()
	disponible = models.BooleanField(default=True)

	def __str__(self):
		return self.nom

class Plat(models.Model):
	menu = models.ForeignKey(Menu, related_name="plats", on_delete=models.CASCADE)
	nom = models.CharField(max_length=10)
	description = models.TextField()
