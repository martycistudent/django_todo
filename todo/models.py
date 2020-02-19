from django.db import models

# Create your models here.
class Item(models.Model):
# Class Item extends from models.Model and Model is a class inside the models module.

    # This is basically the definition of how our table look We've given a
    # name and we've given it two columns, name and done
    # Charfielf - text based input
    name = models.CharField(max_length=30, blank=False)
    # Blank in this instance just means that field will not be nullable when
    # set to false and if we've said true then we would be allowed to have a
    # blank field.
    done = models.BooleanField(blank=False, default=False)

    # Will give us a more readable friendly representation when reviewed in the admin panel
    def __str__(self):
        return self.name
