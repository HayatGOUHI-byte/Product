from django.test import TestCase

from .models import Produit, Categorie
from django.urls import reverse

import time

class ProduitModelTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Électronique")
        self.produit = Produit.objects.create(nom="Laptop", prix=1200.50, categorie=self.categorie)

    def test_produit_creation(self):
        self.assertEqual(self.produit.nom, "Laptop")
        self.assertEqual(self.produit.prix, 1200.50)
        self.assertEqual(self.produit.categorie.nom, "Électronique")




#test d'intégration

class ProduitViewTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Électronique")
        self.produit = Produit.objects.create(nom="Smartphone", prix=800, categorie=self.categorie)

    def test_produit_list_view(self):
        response = self.client.get(reverse('produit-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Smartphone")
        self.assertTemplateUsed(response, 'produit_list.html')

 #test fonctionnels


class ProduitFormTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Mode")

    def test_ajout_produit(self):
        response = self.client.post(reverse('produit-create'), {
            'nom': 'T-shirt',
            'prix': 20.99,
            'categorie': self.categorie.id
        })
        self.assertEqual(response.status_code, 302)  # Redirection après succès
        self.assertTrue(Produit.objects.filter(nom="T-shirt").exists())


 #test de performance , vérifie que certaines requêtes ne dépassent pas certain limite de temps


class PerformanceTest(TestCase):
    def test_produit_list_performance(self):
        start_time = time.time()
        response = self.client.get(reverse('produit-list'))
        end_time = time.time()
        self.assertTrue(end_time - start_time < 0.5)  # Doit répondre en moins de 500ms



# 5️⃣ Tests de Sécurité
# ➡ Vérifier les failles comme l’injection SQL ou XSS.

# 📌 Exemple : Vérifier qu’un utilisateur non autorisé ne peut pas supprimer un produit


class SecurityTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Électronique")
        self.produit = Produit.objects.create(nom="Ordinateur", prix=1000, categorie=self.categorie)

    def test_suppression_non_autorisee(self):
        response = self.client.post(reverse('produit-delete', args=[self.produit.id]))
        self.assertNotEqual(response.status_code, 200)  # Doit refuser l'accès

        