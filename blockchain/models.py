from django.db import models
from django.contrib.auth.models import User
import string
import random


class Shopper(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    user = models.OneToOneField(User, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.user:
            email = str(self.name) + '@gmail.com'
            chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
            password = ''.join(random.choice(chars) for _ in range(8))
            self.user = User.objects.create_user(self.name, email, password)
        super(Shopper, self).save(*args, **kwargs)
