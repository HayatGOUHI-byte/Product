from django import forms
from .models import Produit, Categorie

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'prix', 'categorie']  # Inclure tous les champs
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        empty_label="Sélectionnez une catégorie",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
