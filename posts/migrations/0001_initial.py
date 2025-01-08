# Generated by Django 5.1.4 on 2025-01-07 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]