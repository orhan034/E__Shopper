from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı Adı"), on_delete=models.CASCADE)
    job = models.CharField(("Meslek"), max_length=50, default='-')
    address = models.CharField(("Adres"), max_length=50, default='-')
    deneyim = models.IntegerField(("Deneyim"), default=0)
    image = models.ImageField(("Profil Resmi"), upload_to='product', max_length=None, default='profilresmi.png')
    phone = models.CharField(("Telefon Numarası"), max_length=50)
    web_site = models.URLField(("Web site"), max_length=200, default='-')
    
    def __str__(self):
        return self.user.username
