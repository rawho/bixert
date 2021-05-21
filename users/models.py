from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="profile_pics/default.jpg", upload_to="profile_pics"
    )
    name = models.CharField(null=True, blank=True, max_length=25)
    phone_no = models.CharField(null=True, blank=True, max_length=10)
    company = models.CharField(null=True, blank=True, max_length=50)

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        img = img.convert("RGB")
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
        img.save(self.image.path)

    def __str__(self):
        return f"{self.user.username} Profile"


    
class Messaging(models.Model):
    user_id = models.CharField(null=True, blank=True, max_length=25)
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE)