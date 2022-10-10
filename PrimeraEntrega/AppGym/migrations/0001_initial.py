# Generated by Django 4.1.1 on 2022-10-08 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo", models.IntegerField()),
                ("nombre", models.CharField(max_length=40)),
                ("apellido", models.CharField(max_length=40)),
                ("phone", models.IntegerField()),
                ("direccion", models.CharField(max_length=60)),
                ("cumple", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Entrenador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo", models.IntegerField()),
                ("nombre", models.CharField(max_length=40)),
                ("apellido", models.CharField(max_length=40)),
                ("phone", models.IntegerField()),
                ("direccion", models.CharField(max_length=40)),
                ("cumple", models.DateField(null=True)),
                ("profesion", models.CharField(max_length=40)),
                ("tipo_entrenador", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Rutina",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo_rutina", models.IntegerField()),
                ("tipo_rutina", models.CharField(max_length=40)),
                ("ubicacion", models.CharField(max_length=40)),
                ("rutina", models.CharField(max_length=1000)),
            ],
        ),
    ]
