# Generated by Django 3.2.6 on 2021-08-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_uti', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_cliente', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=60)),
                ('telefone', models.CharField(max_length=11)),
            ],
        ),
    ]
