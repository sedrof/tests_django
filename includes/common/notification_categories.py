from django.db import models


class NotificationCategories(models.IntegerChoices):
    Default = 1
    Events = 2
    Billing = 3
    Transaction = 4
    Contacts = 5
    Campaigns = 6
    Products = 7
