# Generated by Django 4.1 on 2022-09-05 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangogram', '0002_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='djangogram.tag', verbose_name='Tags'),
        ),
    ]
