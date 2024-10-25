# Generated by Django 5.0.1 on 2024-10-23 22:33

import apps.content.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('content_type', models.CharField(choices=[('audio', 'Audio'), ('video', 'Video'), ('document', 'Document'), ('image', 'Image'), ('note', 'Note')], max_length=20)),
                ('file', models.FileField(upload_to=apps.content.models.content_file_path)),
                ('size', models.BigIntegerField(editable=False)),
                ('exclude_from_legacy', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
