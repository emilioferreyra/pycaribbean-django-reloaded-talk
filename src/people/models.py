from django.db import models
from django.utils.safestring import mark_safe

from sorl.thumbnail import ImageField

from .managers import EmployeeManager
from .managers import CustomerManager
from .managers import ContactManager


class PersonType(models.Model):
    """
    Stores person type information. Related objects:
    :model:`people.Person`
    """
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Person Type"
        verbose_name_plural = "Person Types"

    def __str__(self):
        return self.name


class Person(models.Model):
    """
    Stores person information. Related objects:
    :model:`people.PersonType`
    """
    name = models.CharField(max_length=100)
    person_type = models.ForeignKey('PersonType', on_delete=models.PROTECT)
    gender = models.CharField(
        max_length=1,
        choices=(
            ('M', "Male"),
            ('F', "Female"),
        ),
        null=True
    )
    email = models.EmailField(blank=True, verbose_name="e-mail")
    phone_number = models.CharField(help_text='999-999-9999', max_length=12)
    address = models.TextField(blank=True, null=True)
    picture = ImageField(upload_to='people_pictures', null=True, blank=True)
    status_active = models.BooleanField(default=True)
    objects = models.Manager()
    employee = EmployeeManager()
    customer = CustomerManager()
    contact = ContactManager()

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.picture:
            return mark_safe('<img src="%s" width="60" height="75" />' % self.picture.url)
        else:
            return ' '
    image_tag.short_description = "Photo"
    image_tag.allows_tags = True
    image_tag.admin_order_field = 'name'
