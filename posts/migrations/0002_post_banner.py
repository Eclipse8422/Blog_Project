# Generated by Django 5.1.4 on 2025-01-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='mountains.jpg', upload_to=''),
        ),
    ]