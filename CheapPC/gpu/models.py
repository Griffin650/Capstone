from django.db import models

import csv


# model for GPU
class GPU(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField(default=-1)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email


# Populates the DB with data read in from <files/out.csv>
# updated 3/3/21
def populate():
    with open('gpu/files/out.csv', 'r') as file:
        line = csv.reader(file)
        for row in line:
            try:
                new_gpu = GPU(link=row[0], name=row[1], price=row[2][1:])
                new_gpu.save()
            except EOFError:
                print("Error saving value: [" + row[0] + "]")
                return
