# Generated by Django 4.2 on 2024-10-14 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_management', '0002_alter_blogpost_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
