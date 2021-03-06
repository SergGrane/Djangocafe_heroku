# Generated by Django 4.0.2 on 2022-02-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0011_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Contphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.TextField(blank=True, max_length=20)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='call',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='head',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='location',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='open',
        ),
        migrations.AddField(
            model_name='contactus',
            name='city',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contactus',
            name='opendays',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contactus',
            name='openhours',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contactus',
            name='street',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
