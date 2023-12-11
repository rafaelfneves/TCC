# Generated by Django 4.2.7 on 2023-12-11 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('materials', models.CharField(max_length=255)),
                ('weight_grams', models.FloatField()),
            ],
        ),
    ]