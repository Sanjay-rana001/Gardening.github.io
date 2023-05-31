from django.db import models

class services(models.Model):
     id= models.AutoField(primary_key=True)
     name= models.CharField(max_length= 50)
     description = models.TextField(max_length=1000)
     description2 = models.TextField(default=None,blank=True,null=True)
     picture1= models.ImageField(upload_to="service_images")
     picture3= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     picture4= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     picture5= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     picture6= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     picture2= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     def __str__(self):
          return self.name


class Landscping(models.Model):
     id= models.AutoField(primary_key=True)
     name= models.CharField(max_length= 50)
     description = models.TextField(max_length=1000)
     picture1= models.ImageField(upload_to="service_images")
     picture2= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     picture3= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     picture4= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     picture5= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     icon= models.ImageField(upload_to="service_images")

class Pruning(models.Model):
     id= models.AutoField(primary_key=True)
     name= models.CharField(max_length= 50)
     description = models.TextField(max_length=1000)
     picture1= models.ImageField(upload_to="service_images")
     picture2= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     picture3= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     picture4= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     picture5= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
     icon= models.ImageField(upload_to="service_images")

class Planting(models.Model):
        id= models.AutoField(primary_key=True)
        name= models.CharField(max_length= 50)
        description = models.TextField(max_length=1000)
        picture1= models.ImageField(upload_to="service_images")
        picture2= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
        picture3= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
        picture4= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
        picture5= models.ImageField(upload_to="service_images",default=None,blank=True,null=True)
        icon= models.ImageField(upload_to="service_images")    


class Contact(models.Model):
      id = models.AutoField(primary_key = True) 
      name = models.CharField(max_length=50)
      email = models.EmailField(max_length=54)
      subject = models.CharField(max_length=50)
      msgs = models.TextField()
      def __str__(self):
           return self.name
      

class Quote(models.Model):
      id = models.AutoField(primary_key = True) 
      name = models.CharField(max_length=50)
      email = models.EmailField(max_length=54)
      phone = models.CharField(max_length=30,null=True,default="",blank=True)
      service_type = models.CharField(max_length=50)
      msgs = models.TextField(null=True,default="",blank=True)
      def __str__(self):
           return str(self.id) +"-"+ self.name 