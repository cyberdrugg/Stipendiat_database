# Generated by Django 4.1.4 on 2022-12-12 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=100)),
                ("surname", models.TextField()),
                ("image", models.ImageField(upload_to="")),
                (
                    "group",
                    models.CharField(
                        choices=[
                            ("AIN-1-22", "AIN-1-22"),
                            ("AIN-2-22", "AIN-2-22"),
                            ("MIN-1-22", "MIN-1-22"),
                            ("WIN-1-22", "WIN-1-22"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]
