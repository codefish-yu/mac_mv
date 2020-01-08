# Generated by Django 2.2.3 on 2019-08-08 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0003_accesstoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicAccountUser',
            fields=[
                ('open_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('wechat_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meta.WechatUser')),
            ],
        ),
    ]
