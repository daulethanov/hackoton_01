from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_file_extension

TRE = [
    (1, 'Присужден'),
    (2, 'Не присужден')
]
class User(AbstractUser):
    iin = models.IntegerField(default=0)
    patronymic = models.CharField(max_length=40)
    phone_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username


class Document(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='document', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)


class CheckDocument(models.Model):

    Plan = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]

    Actual = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]

    Idea = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]

    user = models.ForeignKey(User, models.CASCADE)
    document = models.ForeignKey(Document, models.CASCADE, verbose_name='просмотреть документ')
    idea = models.IntegerField(choices=Idea, default=1)
    actual = models.IntegerField(choices=Actual, default=1)
    plan = models.IntegerField(choices=Plan, default=1)
    status = models.IntegerField(choices=TRE,  default=2)

    def star(self):
        return (self.actual + self.idea + self.plan) /3

