# Generated by Django 4.2.6 on 2023-12-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('binding_type', models.CharField(max_length=255)),
                ('year_of_publishing', models.IntegerField()),
                ('number_of_pages', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
