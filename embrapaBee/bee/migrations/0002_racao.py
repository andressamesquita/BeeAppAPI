# Generated by Django 2.2.2 on 2019-07-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Racao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingrediente_1', models.CharField(choices=[('SOJA', 'soja'), ('FUBA', 'fuba'), ('MANDIOCA', 'mandioca'), ('BABAÇU', 'babaçu'), ('LEUCENA', 'leucena'), ('PURILAC', 'purilac'), ('ALGAROBA', 'algaroba')], max_length=12)),
                ('ingrediente_2', models.CharField(choices=[('SOJA', 'soja'), ('FUBA', 'fuba'), ('MANDIOCA', 'mandioca'), ('BABAÇU', 'babaçu'), ('LEUCENA', 'leucena'), ('PURILAC', 'purilac'), ('ALGAROBA', 'algaroba')], max_length=12)),
                ('pb_ingr_1', models.FloatField(blank=True, default=None, null=True)),
                ('pb_ingr_2', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
    ]
