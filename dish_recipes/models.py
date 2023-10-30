from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    dish_name = models.CharField(max_length=255)
    composition = models.TextField()
    recipe = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.dish_name}'
