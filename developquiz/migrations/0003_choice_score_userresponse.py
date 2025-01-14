# Generated by Django 5.0.4 on 2024-05-07 15:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developquiz', '0002_remove_choice_score_choice_comment_choice_is_correct'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='score',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developquiz.choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developquiz.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developquiz.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
