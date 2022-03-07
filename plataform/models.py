from django.db import models
from django.conf import settings

class Image(models.Model):
    image = models.ImageField(upload_to='image')

    class Meta:
        verbose_name_plural = 'Imagens'

    def __str__(self) -> str:
        return self.image.url

class City(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Cidades'

    def __str__(self) -> str:
        return self.name

class VisitDay(models.Model):
    day = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Dias de Visitas'
    
    def __str__(self) -> str:
        return self.day

class Time(models.Model):
    time = models.TimeField()

    class Meta:
        verbose_name_plural = 'Horários'

    def __str__(self) -> str:
        return str(self.time)

class Immobile(models.Model):
    choices = (('V', 'Venda'),('A', 'Aluguel'))

    choices_immobile = (('A', 'Apartamento'),('C', 'Casa'))

    images = models.ManyToManyField(Image)
    value = models.FloatField()
    bedrooms = models.IntegerField()
    size = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    street = models.CharField(max_length=50)
    type_operation = models.CharField(max_length=1, choices=choices)
    type_immobile = models.CharField(max_length=1, choices=choices_immobile)
    number = models.IntegerField()
    description = models.TextField()
    visit_day = models.ManyToManyField(VisitDay)
    times = models.ManyToManyField(Time)

    class Meta:
        verbose_name_plural = 'Imóveis'

    def __str__(self) -> str:
        return self.street


class Visit(models.Model):
    choices = (('S', 'Segunda'),
                ('T', 'Terça'),
                ('Q', 'Quarta'),
                ('QI', 'Quinta'),
                ('SE', 'Sexta'),
                ('SA', 'Sabado'),
                ('D', 'Domingo'))

    choices_status = (('A', 'Agendado'),
                      ('F', 'Finalizado'),
                      ('C', 'Cancelado'))
    immobile = models.ForeignKey(Immobile, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    day = models.CharField(max_length=20)
    time = models.TimeField()
    status = models.CharField(max_length=1, choices=choices_status, default="A")

    class Meta:
        verbose_name_plural = 'Visitas'

    def __str__(self) -> str:
        return self.user.username