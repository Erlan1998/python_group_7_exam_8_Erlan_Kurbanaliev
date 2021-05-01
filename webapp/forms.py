from django import forms
from webapp.models import Product


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'image']