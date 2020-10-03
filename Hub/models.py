from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class Movies(models.Model):
    moviename = models.CharField(max_length=30)
    movie_heading = models.CharField(max_length=60)
    movie_review = models.TextField(max_length=500)
    movie_image = models.ImageField(upload_to = 'poster/')

    def __str__(self):
        return self.moviename
class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone, password = None):
        if not email:
            raise ValueError("User must have an Email")
        if not username:
            raise ValueError("User must have an Username")
        if not first_name:
            raise ValueError("User must have an First Name")
        if not last_name:
            raise ValueError("User must have an Last Name")
        if not phone:
            raise ValueError("User must have an Phone")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            phone = phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, first_name, last_name, phone, password = None):

        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            first_name = first_name,
            last_name = last_name,
            phone = phone,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=254,unique=True)
    username = models.CharField(max_length=20,unique=True)
    first_name = models.CharField(verbose_name="first name", max_length=20)
    last_name = models.CharField(verbose_name="last name",max_length=15)
    phone = models.IntegerField(verbose_name="phone",unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add = True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','phone']
    objects = UserManager()

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self,app_lebel):
        return True
