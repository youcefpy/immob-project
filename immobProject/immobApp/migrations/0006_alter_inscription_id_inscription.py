# Generated by Django 4.2.7 on 2023-11-16 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immobApp', '0005_alter_inscription_id_inscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='id_inscription',
            field=models.CharField(default='IMOBDZFRAB3AB83E', editable=False, max_length=20, unique=True),
        ),
    ]
