from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Spell, Wizard
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WandForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# class Wand:
#     def __init__(self, length, core, wood, owner, maker):
#         self.length = length
#         self.core = core
#         self.wood = wood
#         self.owner = owner
#         self.maker = maker

# wands = [
#     Wand('15"', 'thestral hair', 'elder wood', 'Albus Dumbledore', 'Death?'),
#     Wand('12 3/4"', 'dragon heartstring', 'walnut', 'Bellatrix Lestrange', 'Ollivander?'),
#     Wand('12 3/4"', 'unicorn hair', 'ash', 'Cedric Diggory', 'Ollivander'),
#     Wand('11"', 'phoenix feather', 'holly', 'Harry Potter', 'Ollivander'),
#     Wand('13 1/2"', 'yew', 'phoenix feather', 'yew', 'Ollivander'),
# ]

def wizards_index(request):
    wizards = Wizard.objects.all()
    return render(request, 'wizards/index.html', { 'wizards': wizards })

def wizards_detail(request, wizard_id):
    wizard = Wizard.objects.get(id=wizard_id)
    wand_form = WandForm()
    return render(request, 'wizards/detail.html', { 'wizard' : wizard, 'wand_form': wand_form })

def add_wand(request, wizard_id):
    form = WandForm(request.POST)
    if form.is_valid():
        new_wand = form.save(commit=False)
        new_wand.wizard_id = wizard_id 
        new_wand.save() 
    return redirect('detail', wizard_id=wizard_id)

def assoc_spell(request, wizard_id, spell_id):
    Wizard.objects.get(id=wizard_id).spells.add(spell_id)
    return redirect('detail', wizard_id=wizard_id)

def assoc_spell_delete(request, wizard_id, spell_id):
    Wizard.objects.get(id=wizard_id).spells.remove(spell_id)
    return redirect('details', wizard_id=wizard_id)

class WizardCreate(CreateView):
    model = Wizard
    fields = '__all__'
    success_url = '/wizards/'

class WizardUpdate(UpdateView):
    model = Wizard
    fields = ['age', 'house', 'profession']

class WizardDelete(DeleteView):
    model = Wizard
    success_url = '/wizards/'

class SpellList(ListView):
    model = Spell
    template_name = 'spells/index.html'

class SpellDetail(DetailView):
    model = Spell
    template_name = 'spells/detail.html'

class SpellCreate(CreateView):
    model = Spell
    fields = ['name', 'action']

class SpellUpdate(UpdateView):
    model = Spell
    fields = ['name', 'action']

class SpellDelete(DeleteView):
    model = Spell
    success_url = '/spells/'





