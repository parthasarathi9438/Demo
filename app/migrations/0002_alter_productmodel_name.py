# Generated by Django 4.0 on 2022-05-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='name',
            field=models.CharField(default=False, max_length=50, unique=True),
        ),
    ]
