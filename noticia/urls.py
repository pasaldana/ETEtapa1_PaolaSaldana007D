from django.urls import path
from .views import index, form_agreg, mostrar, form_mod, form_del

urlpatterns=[
    path('', index, name="index"),
    path('form_agreg/', form_agreg, name="form_agreg"),
    path('mostrar', mostrar, name="mostrar"),
    path('form_mod/<id>', form_mod, name="form_mod"),
    path('form_del/<id>', form_del, name="form_del") 
]