# Generated by Django 5.2 on 2025-04-24 14:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookreader', '0004_alter_book_book_coverimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
