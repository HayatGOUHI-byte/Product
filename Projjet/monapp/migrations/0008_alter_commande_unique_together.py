# Generated by Django 5.1.5 on 2025-02-10 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0007_alter_commande_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='commande',
            unique_together={('client', 'produit')},
        ),
    ]
