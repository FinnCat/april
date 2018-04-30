from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title   = models.CharField(max_length=255)
    url     = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    votes_total = models.IntegerField(default=1)
    image   = models.ImageField(blank=True, null=True, upload_to='images/')
    icon    = models.ImageField(blank=True, null=True, upload_to='icons/')
    body    = models.TextField(max_length=1000)
    hunter  = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%Y-%m-%d, %H:%M')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:220]
