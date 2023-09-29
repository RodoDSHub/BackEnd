# Generated by Django 4.2.5 on 2023-09-29 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GestorTareas', '0004_alter_tareas_descrip_alter_tareas_titulo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nombre de Usuario'),
        ),
    ]