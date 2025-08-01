# Generated by Django 5.2 on 2025-04-20 05:17

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
                ('title', models.CharField(max_length=40)),
                ('genre', models.CharField(max_length=60)),
                ('des', models.TextField()),
                ('book_coverimage', models.ImageField(upload_to='')),
                ('author', models.CharField(max_length=30)),
            ],
        ),
    ]
