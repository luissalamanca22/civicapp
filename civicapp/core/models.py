# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Timestamped(models.Model):
    """
    """
    ip_creacion = models.GenericIPAddressField(
        verbose_name=("IP de creación"),
        null=True,
        blank=True
    )
    fecha_creacion = models.DateTimeField(
        'Fecha de creacion',
        auto_now_add=True,
        help_text='Fecha hora en que se creó el objeto.'
    )
    ip_modificacion = models.GenericIPAddressField(
        verbose_name=("IP de modificación"),
        null=True,
        blank=True
    )
    fecha_modificacion = models.DateTimeField(
        'Fecha de Modificación',
        auto_now=True,
        help_text='Fecha y hora en que se modificó el objeto por última vez.'
    )

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = 'fecha_creacion'
        ordering = ['-fecha_creacion', '-fecha_modificacion']


class User(Timestamped, AbstractUser):
    """User model.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class Profile(Timestamped, models.Model):
    """Profile model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)

