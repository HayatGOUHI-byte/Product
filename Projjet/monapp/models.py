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
    produit_choisi = models.ForeignKey('Produit', on_delete=models.SET_NULL, null=True,  blank=True, related_name='clients' )

    def __str__(self):
        return f"{self.produit_choisi.nom} - > {self.produit_choisi.categorie.description}"

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



class CustomerUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 128)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

