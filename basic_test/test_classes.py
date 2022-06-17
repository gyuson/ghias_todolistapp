from django.utils import timezone

from django.db import models
from django.urls import reverse
from django.conf import settings

import pytest

settings.configure(DEBUG=True)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

    def test_classes_compare():
        list1 = ToDoList("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum.")
        assert list1.title <= 100
    

