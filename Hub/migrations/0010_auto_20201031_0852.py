# Generated by Django 3.1.1 on 2020-10-31 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0009_auto_20201030_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='date_of_end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='date_of_start',
            field=models.DateField(null=True),
        ),
    ]