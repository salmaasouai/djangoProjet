# Generated by Django 5.1.3 on 2024-12-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionOffres', '0002_offre_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='category',
            field=models.CharField(choices=[('kids', 'Kids'), ('teens', 'Teens'), ('other', 'Other')], max_length=50),
        ),
    ]
