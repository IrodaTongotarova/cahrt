from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add', add, name='add'),
    path('product/<uuid:product_id>/', view, name='arch'),
    path('delete/<uuid:id>', delete, name='add'),
    path('edit/<uuid:id>', edit, name='add'),
    path('edit/editrecord/<uuid:id>', editrecord, name='add' )
    
]