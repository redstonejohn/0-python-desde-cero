# Generated by Django 4.2.7 on 2023-11-20 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=1000)),
                ('category', models.TextField(max_length=200)),
                ('image', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('count', models.IntegerField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticate.articulos')),
            ],
        ),
    ]