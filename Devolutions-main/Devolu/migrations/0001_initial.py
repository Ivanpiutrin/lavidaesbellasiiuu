# Generated by Django 4.1 on 2022-12-10 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomproduct', models.CharField(max_length=100)),
                ('cantidad', models.PositiveIntegerField()),
                ('costo', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Distribuidor', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('nombre_vendedor', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=100)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devolu.cliente')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devolu.producto')),
            ],
        ),
    ]
