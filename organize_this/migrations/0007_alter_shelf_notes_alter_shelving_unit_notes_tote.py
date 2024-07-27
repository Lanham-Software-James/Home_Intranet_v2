# Generated by Django 5.0.7 on 2024-07-27 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organize_this', '0006_rename_shelving_unit_id_shelf_shelving_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelf',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='shelving_unit',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Tote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('notes', models.TextField(blank=True)),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organize_this.shelf')),
            ],
        ),
    ]
