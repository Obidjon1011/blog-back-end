# Generated by Django 2.2.12 on 2022-01-30 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_article_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tag',
            new_name='tags',
        ),
    ]