from django.db import models


class Campaing(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")


class Logo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    logo = models.ImageField(upload_to="images/logo")  # images/logo klasörüne yükler
    searchbackground = models.ImageField(
        upload_to="images/logo"
    )  

    def __str__(self):
        return self.title
