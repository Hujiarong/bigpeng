# Generated by Django 2.2.6 on 2019-10-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='vol',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2, verbose_name='电压'),
        ),
    ]
