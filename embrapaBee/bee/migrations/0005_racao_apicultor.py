# Generated by Django 2.2.2 on 2019-07-24 12:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0004_auto_20190724_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='racao',
            name='apicultor',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='balanceamentos_racoes', to='bee.Apicultor'),
            preserve_default=False,
        ),
    ]
