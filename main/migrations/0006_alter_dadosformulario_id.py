# Generated by Django 5.0.3 on 2024-04-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_dadosformulario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadosformulario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
