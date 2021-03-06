# Generated by Django 3.1.7 on 2021-07-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questioncontribution',
            name='sort_order',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='questioncontribution',
            constraint=models.UniqueConstraint(fields=('base_question', 'contributor', 'sort_order'), name='unique_contribution'),
        ),
    ]
