from django.db import models


d = dict(
    employee=1,
    customer=2,
    contact=3
)


class EmployeeManager(models.Manager):
    """
    Manage Employees query set to only return
    person type = employee
    """

    def get_queryset(self):
        return super(EmployeeManager, self).\
            get_queryset().filter(person_type=d['employee'])


class CustomerManager(models.Manager):
    """
    Manage Customer query set to only return
    person type = customer
    """

    def get_queryset(self):
        return super(CustomerManager, self).\
            get_queryset().filter(person_type=d['customer'])


class ContactManager(models.Manager):
    """
    Manage Contact query set to only return
    person type = contact
    """

    def get_queryset(self):
        return super(ContactManager, self).\
            get_queryset().filter(person_type=d['contact'])