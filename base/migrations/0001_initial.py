# Generated by Django 5.0.7 on 2024-07-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
                ('name', models.CharField(max_length=45)),
                ('uuid', models.UUIDField()),
            ],
        ),
    ]
