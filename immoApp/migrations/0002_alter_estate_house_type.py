# Generated by Django 5.0.4 on 2024-05-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='house_type',
            field=models.TextField(choices=[('1', 'VILLA'), ('2', 'SINGLE_HOUSE'), ('3', 'FARM_HOUSE'), ('4', 'BIFAMILIAR_HOUSE'), ('5', 'ROW_HOUSE'), ('6', 'MULTIPLE_DWELLING'), ('7', 'CHALET'), ('8', 'TERRACE_HOUSE')]),
        ),
    ]