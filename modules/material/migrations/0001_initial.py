# Generated by Django 4.2.7 on 2023-12-11 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('fk_categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.categorymodel')),
            ],
        ),
    ]
