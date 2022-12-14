# Generated by Django 3.2.10 on 2022-12-05 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppRegisteration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MobileNumber', models.IntegerField()),
                ('operator', models.TextField(choices=[('MTC', 'MTC'), ('Touch', 'Touch')], max_length=5)),
                ('AllNotification', models.BooleanField(default=False)),
                ('ImageNotification', models.BooleanField(default=False)),
                ('VideoNotification', models.BooleanField(default=False)),
                ('AudioNotification', models.BooleanField(default=False)),
                ('platform', models.TextField(choices=[('android', 'android'), ('ios', 'ios')], max_length=1000)),
                ('language_code', models.CharField(blank=True, choices=[('en', 'en'), ('ar', 'ar'), ('fr', 'fr')], default='en', max_length=13)),
                ('FirebaseToken', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]
