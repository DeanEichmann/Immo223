from django.db import models

"""
living_space - Denotes the living area of the house in square meters.
number_rooms - Indicates the total number of rooms in the house.
has_balcony - Binary indicator of whether the object has a balcony (Yes/No).
house_type - Describes the type of the house, such as "Villa".
year_built - Represents the year in which the house was constructed.
"""
<<<<<<< HEAD
class Estate(models.Model):
    class HouseType(models.TextChoices):
        VILLA = 'VILLA', 'Villa'
        SINGLE_HOUSE = 'SINGLE_HOUSE', 'Single House'
        FARM_HOUSE = 'FARM_HOUSE', 'Farm House'
        BIFAMILIAR_HOUSE = 'BIFAMILIAR_HOUSE', 'Bifamiliar House'
        ROW_HOUSE= 'ROW_HOUSE', 'Row House'
        MULTIPLE_DWELLING = 'MULTIPLE_DWELLING', 'Multiple Dwelling'
        CHALET = 'CHALET', 'Chalet'
        TERRACE_HOUSE = 'TERRACE_HOUSE', 'Terrace House'
      
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    living_space = models.FloatField()
    number_rooms = models.IntegerField()
    has_balcony = models.BooleanField()
    house_type = models.CharField(choices=HouseType, max_length=100)
=======
class estate(models.Model):
    class HouseType(models.TextChoices):
        VILLA = '1', 'VILLA'
        SINGLE_HOUSE = '2', 'SINGLE_HOUSE'
        FARM_HOUSE = '3', 'FARM_HOUSE'
        BIFAMILIAR_HOUSE = '4', 'BIFAMILIAR_HOUSE'
        ROW_HOUSE= '5', 'ROW_HOUSE'
        MULTIPLE_DWELLING = '6', 'MULTIPLE_DWELLING'
        CHALET = '7', 'CHALET'
        TERRACE_HOUSE = '8', 'TERRACE_HOUSE'
    
    name = models.CharField(max_length=80)
    adress = models.CharField(max_length=30, default='missing')
    living_space = models.FloatField()
    number_rooms = models.IntegerField()
    has_balcony = models.BooleanField()
    house_type = models.TextField(choices=HouseType)
>>>>>>> main
    year_built = models.IntegerField()