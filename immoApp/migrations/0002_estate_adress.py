# Generated by Django 5.0.4 on 2024-05-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='adress',
            field=models.CharField(default='missing', max_length=30),
        ),
    ]