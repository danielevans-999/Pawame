# Generated by Django 2.2 on 2020-01-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
