# Generated by Django 4.1.4 on 2022-12-11 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0005_alter_admin_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institucion',
            name='director',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='institucion',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_nac',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='institucion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tutor',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Institucion',
        ),
        migrations.DeleteModel(
            name='Tipo_user',
        ),
        migrations.DeleteModel(
            name='Tutor',
        ),
    ]
