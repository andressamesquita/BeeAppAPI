# Generated by Django 2.2.2 on 2019-07-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0003_perda_foto_perda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perda',
            name='tipo_perda',
            field=models.CharField(choices=[('POR ABANDONO', 'Abandono de colmeia'), ('POR MORTE', 'Morte')], max_length=20),
        ),
    ]