from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Wizard, Spell, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WandForm

import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'wand-collector'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def wizards_index(request):
    wizards = Wizard.objects.filter(user=request.user)
    return render(request, 'wizards/index.html', { 'wizards': wizards })

@login_required
def wizards_detail(request, wizard_id):
    wizard = Wizard.objects.get(id=wizard_id)
    wand_form = WandForm()
    spells_wizard_doesnt_have = Spell.objects.exclude(id__in = wizard.spells.all().values_list('id'))
    return render(request, 'wizards/detail.html', {'wizard' : wizard, 'wand_form': wand_form, 'spells': spells_wizard_doesnt_have })

@login_required
def add_wand(request, wizard_id):
    form = WandForm(request.POST)
    if form.is_valid():
        new_wand = form.save(commit=False)
        new_wand.wizard_id = wizard_id 
        new_wand.save() 
    return redirect('detail', wizard_id=wizard_id)



@login_required
def assoc_spell(request, wizard_id, spell_id):
    Wizard.objects.get(id=wizard_id).spells.add(spell_id)
    return redirect('detail', wizard_id=wizard_id)

@login_required
def assoc_spell_delete(request, wizard_id, spell_id):
    Wizard.objects.get(id=wizard_id).spells.remove(spell_id)
    return redirect('detail', wizard_id=wizard_id)

@login_required
def add_photo(request, wizard_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, wizard_id=wizard_id)
            photo.save()
        except Exception as error:
            print('Error uploading photo:', error)
            return redirect('detail', wizard_id=wizard_id)
    return redirect('detail', wizard_id=wizard_id)
    
def signup(request):
    error_message = ''
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid Info - Please Try Again"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class WizardCreate(LoginRequiredMixin, CreateView):
    model = Wizard
    fields = ['name', 'age', 'house', 'profession']
    success_url = '/wizards/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WizardUpdate(LoginRequiredMixin, UpdateView):
    model = Wizard
    fields = ['age', 'house', 'profession']

class WizardDelete(LoginRequiredMixin, DeleteView):
    model = Wizard
    success_url = '/wizards/'

class SpellList(LoginRequiredMixin, ListView):
    model = Spell
    template_name = 'spells/index.html'

class SpellDetail(LoginRequiredMixin, DetailView):
    model = Spell
    template_name = 'spells/detail.html'

class SpellCreate(LoginRequiredMixin, CreateView):
    model = Spell
    fields = ['name', 'action']

class SpellUpdate(LoginRequiredMixin, UpdateView):
    model = Spell
    fields = ['name', 'action']

class SpellDelete(LoginRequiredMixin, DeleteView):
    model = Spell
    success_url = '/spells/'





