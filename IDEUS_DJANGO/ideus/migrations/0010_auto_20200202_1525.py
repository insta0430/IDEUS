# Generated by Django 2.2.4 on 2020-02-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideus', '0009_auto_20200202_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.IntegerField(choices=[(2, '디자인'), (0, '기타'), (3, '교육'), (1, '코딩')], default=0),
        ),
    ]
