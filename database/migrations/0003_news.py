# Generated by Django 4.1.4 on 2022-12-13 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0002_alter_student_surname"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=150)),
                ("short", models.CharField(max_length=400)),
                ("content", models.TextField()),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
    ]
