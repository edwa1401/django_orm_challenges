# Generated by Django 4.2.5 on 2023-09-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(choices=[('LENOVO', 'Lenovo'), ('HONOR', 'Honor'), ('APPLE', 'Apple')], max_length=100)),
                ('year_of_issue', models.CharField(help_text='year_of issue', max_length=4)),
                ('ram_volume', models.PositiveSmallIntegerField(help_text='ram volume in GB')),
                ('hdd_capacity', models.DecimalField(decimal_places=3, help_text='hdd capacity in GB', max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_count', models.PositiveSmallIntegerField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('PUBLISHED', 'Published'), ('NOT_PUBLISHED', 'Not Published'), ('BANNED', 'Banned')], default='NOT_PUBLISHED', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField()),
                ('category', models.CharField(choices=[('CL', 'Culture'), ('SP', 'Sport'), ('PL', 'Politic')], max_length=100)),
            ],
            options={
                'ordering': ['-published_at'],
                'get_latest_by': ('published_at',),
            },
        ),
    ]
