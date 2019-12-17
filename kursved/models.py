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
    #id_vedom = models.ForeignKey(vedom, models.PROTECT)
    
    def __str__(self):
        qwe = self.name + ' ' + self.surname + ' ' + self.patronymic
        return (qwe)
        
class studtovedom(models.Model):
    Value = [
        ('Зач', 'Зачет'),
        ('Незач', 'Незачет'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    id_vedom = models.ForeignKey(vedom, models.PROTECT)
    id_stud = models.ForeignKey(stud, models.PROTECT)
    value = models.CharField(max_length=5, choices=Value)
    
    def __str__(self):
        qwe = self.id_stud.name + ' ' + self.id_vedom.name
        return (qwe)