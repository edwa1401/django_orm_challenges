# Generated by Django 4.2.5 on 2023-09-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_laptop_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(null=True),
        ),
    ]
