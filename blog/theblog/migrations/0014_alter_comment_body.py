# Generated by Django 5.1.3 on 2024-11-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_merge_0010_alter_comment_body_0012_post_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(),
        ),
    ]
