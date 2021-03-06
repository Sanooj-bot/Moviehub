# Generated by Django 3.1.1 on 2020-10-21 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0006_auto_20201020_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booked',
            new_name='A1',
        ),
        migrations.AddField(
            model_name='booking',
            name='A2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='A3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='A4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='A5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='B1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='B2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='B3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='B4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='B5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='C1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='C2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='C3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='C4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='C5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='D1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='D2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='D3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='D4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='D5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='E1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='E2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='E3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='E4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='E5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='F1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='F2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='F3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='F4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='F5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='G1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='G2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='G3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='G4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='G5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='H1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='H2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='H3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='H4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='H5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='I1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='I2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='I3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='I4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='I5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='J1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='J2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='J3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='J4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='J5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='Movie_Name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Hub.movies'),
        ),
    ]
