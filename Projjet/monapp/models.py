from django.db import models




class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_ajout = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits',default=1)

    def __str__(self):
        return self.nom

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.nom} - {self.email}"

#la création d'un modèle Commande qui regroupe les deux modèles client et produits c'est bon

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='commandes')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='commandes')
    date_commande = models.DateTimeField(auto_now_add=True)
    quantite = models.PositiveIntegerField()


    class Meta:
        unique_together = ('client','produit')

    def __str__(self):
        return f"Commande de {self.client.nom} - {self.produit.nom}"

