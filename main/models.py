from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Home(models.Model):
    name = models.CharField('Navigation',max_length= 40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Home'

class Phone(models.Model):
    name = models.CharField('Name_of_the_link',max_length= 40)
    number = models.CharField('Phone_number',max_length= 40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Phone'

class Hello(models.Model):
    name = models.CharField('Hello',max_length= 40)
    text = models.TextField('Text')
    begin = models.CharField('Begining text',max_length= 40)
    img = models.ImageField('Image')
    bigimg = models.ImageField('BigImage', upload_to=None)

    def __str__(self):
        return self.name

class Story(models.Model):
    bigimg = models.ImageField('BigImage', upload_to=None)
    title = models.CharField('title',max_length= 40)
    img = models.ImageField('Image')
    subtitle = models.CharField('Begining text',max_length= 200)
    first_text = models.TextField('First_Text')
    second_text = models.TextField('Second_Text')

    def __str__(self):
        return self.title

class Info(models.Model):
    name = models.CharField('Info_Name',max_length= 40)
    info = models.CharField('Info',max_length= 240)

    def __str__(self):
        return self.name

class Partner(models.Model):
    img = models.FileField(upload_to="pictures/%Y/%m/", validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    name = 'images'

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField('Info_Name',max_length= 40)
    title = models.CharField('title',max_length= 240)
    img = models.ImageField('Image')
    bigimg = models.ImageField('BigImage', upload_to=None)

    def __str__(self):
        return self.name
    
class All_Info(models.Model):
    name = models.CharField('Count',max_length= 40)
    info = models.CharField('Info',max_length= 240)

    def __str__(self):
        return self.name
    
class First_Service(models.Model):
    name = models.CharField('Name',max_length= 40)
    price = models.CharField('Price',max_length= 240)
    info = models.TextField('Info')


    def __str__(self):
        return self.name
    
class Second_Service(models.Model):
    name = models.CharField('Name',max_length= 40)
    price = models.CharField('Price',max_length= 240)
    info = models.TextField('Info')


    def __str__(self):
        return self.name
    
class Third_Service(models.Model):
    name = models.CharField('Name',max_length= 40)
    price = models.CharField('Price',max_length= 240)
    info = models.TextField('Info')


    def __str__(self):
        return self.name

class Fourth_Service(models.Model):
    name = models.CharField('Name',max_length= 40)
    price = models.CharField('Price',max_length= 240)
    info = models.TextField('Info')


    def __str__(self):
        return self.name