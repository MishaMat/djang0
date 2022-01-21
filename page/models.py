from django.db import models


# Create your models here.
class Adv(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    create_at = models.DateField()
    expire_at = models.DateField()
    price = models.FloatField(default=0)
    views = models.IntegerField(0)
    status = models.ForeignKey('AdvStatus', default=None, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey('User', default=None, null=True, on_delete=models.CASCADE)
    heading = models.ForeignKey('Heading', default=None, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def uah(self):
        return self.price * 28

    class Meta:
        db_table = 'adv'


class AdvStatus(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'advstatus'


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    tel = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'


class Heading(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'heading'
