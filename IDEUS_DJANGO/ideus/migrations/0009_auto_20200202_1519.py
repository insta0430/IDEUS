# Generated by Django 2.2.4 on 2020-02-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideus', '0008_auto_20200202_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.IntegerField(choices=[(0, '기타'), (2, '디자인'), (1, '코딩'), (3, '교육')], default=0),
        ),
    ]
