# Generated by Django 5.0.3 on 2024-04-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_dadosformulario_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadosformulario',
            name='id',
        ),
        migrations.AlterField(
            model_name='dadosformulario',
            name='codigo_bq',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
