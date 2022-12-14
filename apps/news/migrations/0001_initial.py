# Generated by Django 3.2.10 on 2022-12-05 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last', models.BooleanField(default=True)),
                ('local', models.BooleanField(default=False)),
                ('international', models.BooleanField(default=False)),
                ('sport', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_url', models.FileField(upload_to=None)),
                ('media_type', models.CharField(choices=[('Image', 'image'), ('Audio', 'audio'), ('Video', 'video'), ('NoMedia', 'nomedia')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('title', models.TextField(max_length=150)),
                ('discription', models.CharField(max_length=255)),
                ('fb_link', models.URLField()),
                ('thumb', models.FileField(upload_to=None)),
                ('language_code', models.CharField(blank=True, choices=[('en', 'en'), ('ar', 'ar'), ('fr', 'fr')], default='en', max_length=13)),
                ('is_puplished', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('platform', models.TextField(choices=[('android', 'android'), ('ios', 'ios')], max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.media')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
