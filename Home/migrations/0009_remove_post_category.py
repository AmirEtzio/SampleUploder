# Generated by Django 5.1.1 on 2024-10-02 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_alter_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
