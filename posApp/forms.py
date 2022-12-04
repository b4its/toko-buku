from django import forms
from .models import Products
from setuptools import Require

class produk_form(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    category_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gambar = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    stok = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


class produk_for(forms.ModelForm):
     class Meta:
        model = Products
        fields = [ 'code','name','category_id','gambar','description','price','stok' ]
        widgets = {
            
        }

from django import forms

class pembayaran(forms.Form):
  nama_produk = forms.CharField(max_length=100)
  transaksi = forms.CharField(max_length=100)
  jumlah = forms.CharField(max_length=100)

