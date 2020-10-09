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
class Booking(models.Model):
    Customer_Name  = models.ForeignKey(User, null = True, on_delete = models.SET_NULL ,blank= True)
    Movie_Name = models.ForeignKey(Movies, null=True,on_delete = models.SET_NULL, blank= True)
    A1 = models.BooleanField(default = False)
    A2 = models.BooleanField(default = False)
    A3 = models.BooleanField(default = False)
    A4 = models.BooleanField(default = False)
    A5 = models.BooleanField(default = False)

    B1 = models.BooleanField(default = False)
    B2 = models.BooleanField(default = False)
    B3 = models.BooleanField(default = False)
    B4 = models.BooleanField(default = False)
    B5 = models.BooleanField(default = False)

    C1 = models.BooleanField(default = False)
    C2 = models.BooleanField(default = False)
    C3 = models.BooleanField(default = False)
    C4 = models.BooleanField(default = False)
    C5 = models.BooleanField(default = False)

    D1 = models.BooleanField(default = False)
    D2 = models.BooleanField(default = False)
    D3 = models.BooleanField(default = False)
    D4 = models.BooleanField(default = False)
    D5 = models.BooleanField(default = False)

    E1 = models.BooleanField(default = False)
    E2 = models.BooleanField(default = False)
    E3 = models.BooleanField(default = False)
    E4 = models.BooleanField(default = False)
    E5 = models.BooleanField(default = False)

    F1 = models.BooleanField(default = False)
    F2 = models.BooleanField(default = False)
    F3 = models.BooleanField(default = False)
    F4 = models.BooleanField(default = False)
    F5 = models.BooleanField(default = False)

    G1 = models.BooleanField(default = False)
    G2 = models.BooleanField(default = False)
    G3 = models.BooleanField(default = False)
    G4 = models.BooleanField(default = False)
    G5 = models.BooleanField(default = False)

    H1 = models.BooleanField(default = False)
    H2 = models.BooleanField(default = False)
    H3 = models.BooleanField(default = False)
    H4 = models.BooleanField(default = False)
    H5 = models.BooleanField(default = False)

    I1 = models.BooleanField(default = False)
    I2 = models.BooleanField(default = False)
    I3 = models.BooleanField(default = False)
    I4 = models.BooleanField(default = False)
    I5 = models.BooleanField(default = False)

    J1 = models.BooleanField(default = False)
    J2 = models.BooleanField(default = False)
    J3 = models.BooleanField(default = False)
    J4 = models.BooleanField(default = False)
    J5 = models.BooleanField(default = False)

   
