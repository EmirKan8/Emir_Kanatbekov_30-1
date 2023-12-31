# Generated by Django 4.2.3 on 2023-07-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('rate', models.FloatField()),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
