from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid

class UserManager(BaseUserManager):
    """Controlador de usuarios"""

    def create_user(self, email, password, **extra_fields):
        """ Crea un nuevo usuario """
        if not email:
            raise ValueError('Usuarios tiene que tener email')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """ Crea un super usuario """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Modelo de Usuarios"""

    email = models.EmailField('Email', max_length=255,
                              unique=True, default=uuid.uuid1)
    username = models.CharField(max_length=150)
    first_name = models.CharField('Nombre', max_length=30, blank=True)
    last_name = models.CharField('Apellidos', max_length=150, blank=True)
    is_active = models.BooleanField('Activo', default=True)
    is_staff = models.BooleanField('Moderador', default=False)
    date_joined = models.DateField(
        'Día de la creación del usuario', auto_now=False, auto_now_add=True, null=True, blank=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    USERNAME_FIELD = 'email'