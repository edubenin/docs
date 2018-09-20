from django.db import models

# Quartiers
class Neighborhood(models.Model):
    name = models.CharField(max_length=25, primary_key=True) 


# Arrondissements
class District(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    neighborhoods = models.ManyToManyField(Neighborhood)
    

# Communes ~ Ville
class City(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    districts = models.ManyToManyField(District)


# Departements
class Province(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    cities = models.ManyToManyField(City)


# Etablissements d'enseignement supérieur
class University(models.Model):
    STATUS_CHOICES = [
        ('public', 'public'),
        ('private', 'private')
    ]
    name = models.CharField(max_length=25, primary_key=True)
    fullname = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    url = models.URLField()
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    cities = models.ManyToManyField(City)


class Field(models.Model):
    name = models.CharField(max_length=25, primary_key=True)

class Profession(models.Model):
    name = models.TextField(primary_key=True)

class Faculty(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    fullname = models.CharField(max_length=25)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    fields = models.ManyToManyField(Field)

class Course(models.Model):
    name = models.TextField(primary_key=True)
    description = models.TextField()
    prerequisite = models.CharField(max_length=25)
    yearsofstudy = models.CharField(max_length=25)
    faculty = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    fields = models.ManyToManyField(Field)
    professions = models.ManyToManyField(Profession)


class Emergency(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    phone = models.CharField(max_length=25)