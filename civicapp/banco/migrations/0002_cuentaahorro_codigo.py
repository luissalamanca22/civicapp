# Generated by Django 3.0.8 on 2020-07-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuentaahorro',
            name='codigo',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
