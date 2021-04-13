from django.db import models

# Create your models here.
class Image(models.Model):
    img_title = models.CharField(max_length =60)
    img_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')

    @classmethod
    def search_by_title(cls,search_term):
        my_img = cls.objects.filter(img_title__icontains=search_term)
        return my_img