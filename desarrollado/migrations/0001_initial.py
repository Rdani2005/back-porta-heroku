# Generated by Django 4.0.3 on 2022-03-21 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('direccion_imagen', models.TextField()),
                ('tipo_trabajo', models.CharField(choices=[('PROJECT', 'Proyecto'), ('COTIDIANOS', 'Cotidianos'), ('TAREAS', 'Tareas')], default='COTIDIANOS', max_length=10)),
                ('descripcion', models.TextField()),
                ('direccion', models.TextField()),
                ('publicado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]