from django.db import models
from django.contrib.auth.models import User

class vedom(models.Model):
    Types = [
        ('Зач', 'Зачет'),
        ('Диф', 'Диференцируемый зачет'),
        ('Экз', 'Экзамен'),
    ]
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=3, choices=Types)
    id_user = models.ForeignKey(User, models.PROTECT)
    
    def __str__(self):
        return self.name
        
class stud(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    
    def __str__(self):
        qwe = self.name + ' ' + self.surname + ' ' + self.patronymic
        return (qwe)
        
class studtovedom(models.Model):
    Value = [
        ('Зач', 'Зачет'),
        ('Незач', 'Незачет'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    vedomname = models.ForeignKey(vedom, models.PROTECT)
    studname = models.ForeignKey(stud, models.PROTECT)
    value = models.CharField(max_length=5, choices=Value)
    
    def __str__(self):
        qwe = self.studname.name + ' ' + self.vedomname.name
        return (qwe)