# Generated by Django 5.1 on 2024-09-02 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereço', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('curso', models.CharField(max_length=100)),
            ],
        ),
    ]
