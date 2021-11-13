from django.db import models as milan
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customer(AbstractUser):

    def get_absolute_url(self):
        return reverse('account:home-page')
