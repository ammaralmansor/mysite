# Generated by Django 4.1.3 on 2022-12-07 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('title', models.TextField(max_length=150)),
                ('discription', models.CharField(max_length=255)),
                ('thumb', models.FileField(upload_to=None)),
                ('fb_link', models.URLField()),
                ('language_code', models.CharField(blank=True, choices=[('en', 'en'), ('ar', 'ar'), ('fr', 'fr')], default='en', max_length=13)),
                ('is_puplished', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('platform', models.TextField(choices=[('android', 'android'), ('ios', 'ios')], max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdby', to=settings.AUTH_USER_MODEL)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.media')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.RemoveField(
            model_name='tracking',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='tracking',
            name='modified_by',
        ),
        migrations.AddField(
            model_name='appregisteration',
            name='AllNotification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appregisteration',
            name='AudioNotification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appregisteration',
            name='FirebaseToken',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='appregisteration',
            name='ImageNotification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appregisteration',
            name='MobileNumber',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appregisteration',
            name='VideoNotification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appregisteration',
            name='language_code',
            field=models.CharField(blank=True, choices=[('en', 'en'), ('ar', 'ar'), ('fr', 'fr')], default='en', max_length=13),
        ),
        migrations.AddField(
            model_name='appregisteration',
            name='operator',
            field=models.TextField(choices=[('MTC', 'MTC'), ('Touch', 'Touch')], default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appregisteration',
            name='platform',
            field=models.TextField(choices=[('android', 'android'), ('ios', 'ios')], default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='New',
        ),
        migrations.DeleteModel(
            name='Tracking',
        ),
    ]
