# Generated by Django 5.0.4 on 2024-05-07 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developquiz', '0003_choice_score_userresponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userresponse',
            old_name='choice',
            new_name='selected_choice',
        ),
    ]