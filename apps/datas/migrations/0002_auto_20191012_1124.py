# Generated by Django 2.2.6 on 2019-10-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grounddata',
            name='tu_shidu',
            field=models.DecimalField(decimal_places=1, max_digits=10, verbose_name='土壤湿度'),
        ),
        migrations.AlterField(
            model_name='grounddata',
            name='tu_wendu',
            field=models.DecimalField(decimal_places=1, max_digits=10, verbose_name='土壤温度'),
        ),
    ]
