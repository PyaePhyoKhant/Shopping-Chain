import factory
from blockchain.models import Shopper
import random


class ShopperFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Shopper

    name = factory.Faker('name')
    phone = '09' + ''.join([random.choice('0123456789') for _ in range(9)])
