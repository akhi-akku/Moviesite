# Generated by Django 5.0.1 on 2024-02-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0006_alter_movies_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='rls_date',
            field=models.DateTimeField(),
        ),
    ]
