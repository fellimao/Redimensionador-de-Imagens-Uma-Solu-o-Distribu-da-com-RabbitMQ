# Generated by Django 4.1.6 on 2023-02-05 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imaging', '0004_alter_imagem_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
