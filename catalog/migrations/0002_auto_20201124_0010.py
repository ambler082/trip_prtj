# Generated by Django 2.2.5 on 2020-11-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='party_number',
            field=models.IntegerField(default=0),
        ),
    ]