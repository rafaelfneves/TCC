# Generated by Django 4.2.7 on 2023-12-11 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_alter_usermodel_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('requirement', models.CharField(max_length=255)),
                ('points', models.IntegerField()),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usermodel')),
            ],
        ),
    ]