# Generated by Django 2.2.6 on 2019-10-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controleexel',
            name='auto_flag',
            field=models.SmallIntegerField(choices=[(1, '自动'), (0, '手动')], default=0),
        ),
    ]