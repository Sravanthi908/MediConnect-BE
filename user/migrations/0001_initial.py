# Generated by Django 5.2.4 on 2025-07-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('userName', models.CharField(max_length=20, unique=True)),
                ('dob', models.CharField(max_length=8)),
                ('mobile', models.IntegerField(max_length=10)),
            ],
        ),
    ]
