# Generated by Django 4.0.6 on 2022-07-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_wizard_delete_wand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.CharField(max_length=100)),
                ('core', models.CharField(max_length=100)),
                ('wood', models.CharField(max_length=100)),
            ],
        ),
    ]
