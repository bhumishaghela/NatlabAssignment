# Generated by Django 3.2.6 on 2021-08-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=122)),
                ('password', models.TextField(max_length=122)),
            ],
        ),
    ]
