# Generated by Django 4.2.6 on 2023-11-29 01:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("kouryaku", "0004_remove_article_author_remove_article_content_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Article",
            new_name="Articles",
        ),
    ]
