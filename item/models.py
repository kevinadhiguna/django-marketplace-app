from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255)
  
  class Meta:
    verbose_name_plural = 'categories' # Fixes 'Categorys' to 'Categories'
  
  def __str__ (self):
    return self.name # In order to display 'name' property of Category model, instead of hard-string 'Category object (1)' in the admin panel
