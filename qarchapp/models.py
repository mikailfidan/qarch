from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(max_length=1000, blank=True, null=True)
    photo = models.ImageField(upload_to="post", max_length=100, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True, auto_now=True)
    updated_at= models.DateField(blank=True, null=True, auto_now_add=True)

    class Meta:
        verbose_name = "İçerik"
        verbose_name_plural = "İçerikler"
        ordering = ["created_at"]
    
    def __str__(self):
        return self.title



class Information(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to="info", blank=True, null=True)
    motto = models.TextField(max_length=1000, blank=True, null=True)
    introduction_text = models.TextField(max_length = 1000, blank=True, null=True)
    
    class Meta:
        verbose_name="Site Bilgisi"
        verbose_name_plural = "Site Bilgileri"
   
    def __str__(self):
        return self.title    

class Message(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=1000, blank=True, null=True)
