from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Spell(models.Model):
    name = models.CharField(max_length=100)
    action = models.TextField(max_length=500)
    

    def __str__(self):
        return f"{self.name} {self.action}"
    
    def get_absolute_url(self):
        return reverse('spells_detail', kwargs={'pk': self.id})


class Wizard(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    house = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    spells = models.ManyToManyField(Spell)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'wizard_id': self.id})


class Wand(models.Model):
    length = models.CharField(max_length=100)
    core = models.CharField(max_length=100)
    wood = models.CharField(max_length=100)
  
    wizard = models.ForeignKey(Wizard, on_delete=models.CASCADE)
    def __str__(self):
        return f"Wand Description: {self.length} {self.core} {self.wood}"

class Photo(models.Model):
    url = models.CharField(max_length=200)
    wizard = models.ForeignKey(Wizard, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for wizard_id: {self.wizard_id} @{self.url}"