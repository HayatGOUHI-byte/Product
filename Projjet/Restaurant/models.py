from django.db import models
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
	prix = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return self.nom

class Client(models.Model):
	nom = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	telephone = models.CharField(max_length=20)
	adresse = models.TextField()

	def __str__(self):
		return self.nom

class Commande(models.Model):
	client = models.ForeignKey(Client, related_name="commandes", on_delete = models.CASCADE)
	plat = models.ManyToManyField(Plat, related_name="commandes")
	date_commande = models.DateTimeField(auto_now=True)
	statut = models.CharField(max_length=50, default="En attente")

	def __str__(self):
		return f"commande {self.id} pour {self.client.nom}"