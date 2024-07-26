# Generated by Django 5.0.7 on 2024-07-26 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organize_this', '0004_alter_shelving_unit_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('notes', models.TextField()),
                ('shelving_unit_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organize_this.shelving_unit')),
            ],
        ),
    ]
