from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wizards/', views.wizards_index, name='index'),
    path('wizards/<int:wizard_id>/', views.wizards_detail, name='detail'),
    path('wizards/create', views.WizardCreate.as_view(), name='wizards_create'),
    path('wizards/<int:pk>/update', views.WizardUpdate.as_view(), name='wizards_update'),
    path('wizards/<int:pk>/delete', views.WizardDelete.as_view(), name='wizards_delete'),
    path('wizards/<int:wizard_id>/add_wand/', views.add_wand, name='add_wand'),
    path('spells/', views.SpellList.as_view(), name='spells_index'),
    path('spells/<int:pk>/', views.SpellDetail.as_view(), name='spells_detail'),
    path('spells/create/', views.SpellCreate.as_view(), name='spells_create'),
    path('spells/<int:pk>/update/', views.SpellUpdate.as_view(), name='spells_update'),
    path('spells/<int:pk>/delete/', views.SpellDelete.as_view(), name='spells_delete'),
]

