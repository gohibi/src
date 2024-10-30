# Generated by Django 5.1.2 on 2024-10-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='can_preview',
            field=models.BooleanField(default=False, help_text='If user does not have access to course, can they see this ?'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='status',
            field=models.CharField(choices=[('pub', 'Published'), ('soon', 'Coming Soon'), ('draft', 'Draft')], default='draft', max_length=10),
        ),
    ]