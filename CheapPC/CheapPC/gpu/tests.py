from django.test import TestCase
from .models import GPU, add_gpu
import string
import random


def create_gpu(name, price, link):
    return GPU.objects.create(name=name, price=price, link=link)


class CreatedGPU(TestCase):
    def test_create_gpu(self):
        name = ''.join(random.choices(string.ascii_uppercase +
                                      string.digits, k=10))
        price = random.randrange(0, 1000, 1)
        link = ''.join(random.choices(string.ascii_uppercase +
                                      string.digits, k=10))
        test = create_gpu(name, price, link)
        self.assertEqual(test.name == name, True)
        self.assertEqual(test.price == price, True)
        self.assertEqual(test.link == link, True)


