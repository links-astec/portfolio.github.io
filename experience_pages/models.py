from django.db import models


class Experience(models.Model):
    Experience_choices =[
      ('category','Category') ,
      ('organization','Organization'),
      ('role','Role') 
    ]

    category= models.CharField( max_length=80,default='action')
    organization = models.CharField( max_length=80,default='action')
    role = models.TextField(null=True,blank=True)
     
     
    def __str__(self):
        return self.category
