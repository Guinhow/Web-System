# Generated by Django 5.0.3 on 2024-04-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_dadosformulario_id_alter_dadosformulario_codigo_bq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadosformulario',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]