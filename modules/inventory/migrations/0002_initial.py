# Generated by Django 4.2.7 on 2023-12-11 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorymodel',
            name='fk_materials',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.materialmodel'),
        ),
    ]