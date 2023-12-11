from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    gender_choices=(('M', 'Male'),
                    ('F', 'Female'),
                    ('N/A', 'No answers'))
    user = models.OneToOneField(User,on_delete=models.CASCADE,
                                primary_key=True)
    nickname = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    gender = models.CharField(choices=gender_choices,max_length=25)
    account_image = models.ImageField(default='default.jpg',
                                      upload_to='account_images')
    address = models.CharField(max_length=100)
    vk = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nickname}'s account"

    class Meta:
        ordering = ['user']
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


