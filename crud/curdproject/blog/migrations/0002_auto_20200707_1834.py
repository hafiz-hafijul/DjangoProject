# Generated by Django 3.0.6 on 2020-07-07 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='sur_name',
            new_name='sure_name',
        ),
    ]