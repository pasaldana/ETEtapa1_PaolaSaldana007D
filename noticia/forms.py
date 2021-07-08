from django import forms
from django.forms import ModelForm,widgets
from .models import Registro, Categoria

class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = ['rut','foto','nombre','telefono','direccion','email','pais', 'categoria']
        labels={
            'rut':'Rut del colaborador',
            'foto':'Fotografía que lo identifique',
            'nombre':'Nombre completo',
            'telefono':'Teléfono',            
            'direccion':'Dirección', 
            'email':'E-mail',            
            'pais':'País',
            'categoria':'Tipo de sugerencia'
        }

        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'rut',
                    'name': 'rut',
                    'placeholder': '12.3456.789-0'
                }
            ),
            'foto': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'foto',
                    'name': 'foto',
                    'placeholder': 'Fotografía que lo identifique'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'name': 'nombre',
                    'id': 'nombre',
                    'placeholder': 'Ingrese su nombre completo'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'telefono',
                    'name': 'telefono',
                    'placeholder': 'Ingrese su número de contacto',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'direccion',
                    'name': 'direccion',
                    'placeholder': 'Ingrese su dirección'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'email',
                    'name': 'email',
                    'placeholder': 'Nombre@dominio.cl'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'pais',
                    'name': 'pais',
                    'placeholder': 'Ingrese su país'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'controls',
                    'id': 'telefono',
                    'name': 'categoria'
                }
            ),        
        }

