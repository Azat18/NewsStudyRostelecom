# Generated by Django 4.2.6 on 2023-12-02 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_tag_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
