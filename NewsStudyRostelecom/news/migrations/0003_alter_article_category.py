# Generated by Django 4.2.6 on 2023-12-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_status_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('C', 'Культура'), ('B', 'Бизнес'), ('S', 'Наука'), ('N', 'Спорт'), ('T', 'Путешествия'), ('W', 'Погода')], max_length=25, verbose_name='Категории'),
        ),
    ]
