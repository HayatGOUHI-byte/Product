# Generated by Django 5.1.5 on 2025-02-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0003_produit_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
