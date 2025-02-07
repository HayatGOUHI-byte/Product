from django.core.management.base import BaseCommand
from monapp.models import Categorie

class Command(BaseCommand):
    help = "Ajoute un grand nombre de catégories à la base de données"

    def handle(self, *args, **kwargs):
        # Génération d'une liste massive de catégories
        categories = [
            Categorie(
                nom=f"Catégorie {i}",
                description=f"Description de la catégorie {i}"
            )
            for i in range(1, 10001)  # Par exemple, 10 000 catégories
        ]

        # Insertion en une seule requête
        Categorie.objects.bulk_create(categories)

        self.stdout.write(self.style.SUCCESS("Catégories ajoutées avec succès !"))
