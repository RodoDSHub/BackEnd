# Generated by Django 4.2.5 on 2023-09-27 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestorTareas', '0003_remove_integrantes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='descrip',
            field=models.CharField(max_length=200, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestorTareas.usuarios', verbose_name='Nombre de Usuario'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(max_length=32, verbose_name='Nombre de Usuario'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='password',
            field=models.CharField(max_length=16, verbose_name='Contraseña'),
        ),
    ]