# Generated by Django 4.2.6 on 2023-11-29 01:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("kouryaku", "0003_comments"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="author",
        ),
        migrations.RemoveField(
            model_name="article",
            name="content",
        ),
        migrations.RemoveField(
            model_name="article",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="article",
            name="updated_at",
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
    ]