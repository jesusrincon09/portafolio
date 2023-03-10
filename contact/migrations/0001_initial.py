# Generated by Django 4.1.6 on 2023-02-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('email', models.EmailField(max_length=254, verbose_name='correo')),
                ('phone', models.PositiveIntegerField(verbose_name='Telefono')),
                ('whatsapp', models.PositiveIntegerField(verbose_name='whatsapp')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'ordering': ['-created'],
            },
        ),
    ]
