from django.db import models

class Bank(models.Model):
    """
    Banks table consists on name and auto increment id
    """
    name = models.CharField(max_length= 49)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{}".format(self.name)


class Branch(models.Model):
    """
    Branches table consisting columns as declared below
    """
    name = models.CharField(max_length=256)
    bank = models.ForeignKey(Bank, on_delete =models.CASCADE)
    ifsc = models.CharField(max_length= 11, primary_key=True)
    branch = models.CharField(max_length= 74)
    address = models.CharField(max_length= 195)
    city = models.CharField(max_length= 50)
    district = models.CharField(max_length= 50)
    state = models.CharField(max_length= 26)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Branch'
        verbose_name_plural = 'Branch'


    def __str__(self):
        return "{} - {} - {}".format(self.name, self.city, self.bank)
