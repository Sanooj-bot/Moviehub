# Generated by Django 3.1.1 on 2020-11-02 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0010_auto_20201031_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='movie_heading',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='movie_review',
            field=models.TextField(max_length=500, null=True),
        ),
    ]