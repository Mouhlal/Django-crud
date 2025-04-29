# forms.py
from django import forms
from .models import Book , Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        # Les champs que tu veux afficher dans le formulaire
        #fields = ['name','email','bio','annee_naissance']  
        fields = '__all__'  
        widgets = {
            'name' :forms.TextInput(attrs={'placeholder': 'Nom de l\'auteur'}),
            'email' :forms.TextInput(attrs={'placeholder': 'Email de l\'auteur'}),
            'bio' :forms.Textarea(attrs={'placeholder': 'Biographie de l\'auteur'}),
            'annee_naissance' :forms.TextInput(attrs={'placeholder': 'Année de naissance de l\'auteur'}),
            'annee_naissance': forms.DateInput(attrs={'type': 'date'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # Les champs que tu veux afficher dans le formulaire
        fields = ['title','author','publication_date']
        widgets = {
            'title' :forms.TextInput(attrs={'placeholder': 'Titre du livre'}),
            'author' :forms.Select(attrs={'placeholder': 'Auteur du livre'}),
            'publication_date' :forms.TextInput(attrs={'placeholder': 'Date de publication'}),
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
        # Utiliser un widget de type date pour le champ publication_date
        # Cela affichera un sélecteur de date dans le formulaire