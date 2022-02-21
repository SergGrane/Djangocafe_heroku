# Generated by Django 4.0.2 on 2022-02-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0015_slides'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True, max_length=500)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]