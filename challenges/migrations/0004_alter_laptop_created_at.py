# Generated by Django 4.2.5 on 2023-09-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_alter_post_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
