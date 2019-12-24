from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/',blank = True,null = True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={"pk": self.pk})  # detail is url on urls.py
