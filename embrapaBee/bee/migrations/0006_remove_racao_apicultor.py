# Generated by Django 2.2.2 on 2019-07-24 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0005_racao_apicultor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='racao',
            name='apicultor',
        ),
    ]
