from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 300)
    
    def __str__(self):
        return f"{self.name}({self.address})"
    
    # one-to-one
    # many-to-many

class Participant(models.Model):
    email = models.EmailField(unique = "True")

    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length = 200)
    organizer_email = models.EmailField()
    date = models.DateField(default='2021-04-12')
    slug = models.SlugField(unique = True)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    location = models.ForeignKey(Location,on_delete = models.CASCADE,default="New York")
    participent = models.ManyToManyField(Participent,blank = True)
    def __str__(self):
        return f"{self.title} - {self.slug}"
    