from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class Main(models.Model):
    data = models.DateField(auto_now=True)
    name = models.CharField(max_length=150)
    brand = models.TextField()
    price = models.IntegerField()
    quanity = models.IntegerField()
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False, unique=True)

    def __str__(self):
        return self.name
    
    def link(self):
        return reverse('arch', kwargs={'product_id': self.pk})