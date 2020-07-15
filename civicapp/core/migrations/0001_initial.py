# Generated by Django 3.0.8 on 2020-07-13 21:16

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP de creación')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, help_text='Fecha hora en que se creó el objeto.', verbose_name='Fecha de creacion')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP de modificación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modificó el objeto por última vez.', verbose_name='Fecha de Modificación')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.', regex='\\+?1?\\d{9,15}$')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-fecha_creacion', '-fecha_modificacion'],
                'get_latest_by': 'fecha_creacion',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP de creación')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, help_text='Fecha hora en que se creó el objeto.', verbose_name='Fecha de creacion')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP de modificación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modificó el objeto por última vez.', verbose_name='Fecha de Modificación')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/pictures/', verbose_name='profile picture')),
                ('biography', models.TextField(blank=True, max_length=500)),
                ('age', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-fecha_creacion', '-fecha_modificacion'],
                'get_latest_by': 'fecha_creacion',
                'abstract': False,
            },
        ),
    ]
