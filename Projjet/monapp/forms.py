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


#*****On crée le formulaire de la recherche de la catégorie par l'utilisateru puis  la recherche est lancée

class RechercheCategorieForm(forms.Form):
    nom_categorie = forms.CharField(
        label="Nom de la catégorie",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom de la catégorie'})
    )


class OrdreForm(forms.Form):
    COLONNES = [ 
    ('nom', 'Nom'),
    ('description','Description'),
    ]
    colonne = forms.ChoiceField(choices=COLONNES, label="Trier Par")

#Contact form

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100,label = "Nom" )
    email = forms.EmailField(label = "Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")

