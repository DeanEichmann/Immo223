from django.db import models

"""
living_space - Denotes the living area of the house in square meters.
number_rooms - Indicates the total number of rooms in the house.
has_balcony - Binary indicator of whether the object has a balcony (Yes/No).
house_type - Describes the type of the house, such as "Villa".
year_built - Represents the year in which the house was constructed.
"""
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
    year_built = models.IntegerField()