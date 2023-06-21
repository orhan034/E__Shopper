from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    slug = models.SlugField(("Slug Kategori"), blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title

class Gander(models.Model):
    title = models.CharField(("Cinsiyet"), max_length=50)
    slug = models.SlugField(("Slug Kategori"), blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gander, self).save(*args, **kwargs)
    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(("Beden"), max_length=50)
    slug = models.SlugField(("Slug Beden"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Size, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class ProductTuru(models.Model):
    title = models.CharField(("Ürün Türü"), max_length=50)
    slug = models.SlugField(("Slug Beden"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ProductTuru, self).save(*args, **kwargs)

    def __str__(self):
        return self.title 

class Product(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    title = models.CharField(("Başlık"), max_length=50)
    brand = models.CharField(("Marka"), max_length=50)
    text = models.TextField(("Açıklama"), max_length=1000)
    detail = models.TextField(("Özellikler"), max_length=800)
    gander = models.ForeignKey(Gander, verbose_name=("Cinsiyet"), on_delete=models.CASCADE, null=True)
    stars = models.FloatField(("Puan"), default=0)
    image = models.ImageField(("Resim"), upload_to="product", null=True)
    slug = models.SlugField(("Slug Title"), blank=True, null=True)
    productTuru = models.ForeignKey(ProductTuru, verbose_name=("Ürün Türü"), on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title

class ProductImg(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    image = models.ImageField(("Resim"), upload_to="product")
    
    def __str__(self):
        return self.product.title

class SizeLetter(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    price = models.FloatField(("Fiyat"),default=0)
    stok = models.IntegerField(("Stok"), default=0)
    size = models.ForeignKey(Size, verbose_name=("Beden"), on_delete=models.CASCADE,null=True, blank=True)
    

    def __str__(self):
        return self.product.title 
    
class ProductStok(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    images = models.ManyToManyField(ProductImg, verbose_name=("Ürün Fotoğrafları"))
    sizeletter = models.ManyToManyField(SizeLetter, verbose_name=("Kıyafet beden ve stok"), blank=True)
    
    def __str__(self):
        return self.product.title

class ShopBasket(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    sizeletter = models.ForeignKey(SizeLetter, verbose_name=("Ürün"), on_delete=models.CASCADE)
    price_all = models.FloatField(("Toplam Fiyat"), default=0)
    count = models.IntegerField(("Toplam Adet"), default=0)
    date_now = models.DateField(("Saat"), auto_now_add=True, null=True)

    def __str__(self):
        return self.sizeletter.product.title
    

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yurum"), max_length=1000)
    date_now = models.DateTimeField(("Tarih"), auto_now_add=True)
    star = models.IntegerField(("Yorum Puanı"), default=5)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(("İsim"), max_length=50)
    email = models.CharField(("Email"), max_length=50)
    title = models.CharField(("Mesaj Başlığı"), max_length=50)
    text = models.TextField(("Mesaj"), max_length=1000)

    def __str__(self):
        return self.title