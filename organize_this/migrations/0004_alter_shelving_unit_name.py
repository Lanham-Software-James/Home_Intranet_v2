# Generated by Django 5.0.7 on 2024-07-26 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organize_this', '0003_alter_shelving_unit_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelving_unit',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
