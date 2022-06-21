from django.db import models


class SupportedLanguages(models.TextChoices):
    EN = "en"
    ES = "es"
    FR = "fr"
    PT = "pt"
    ZhHans = "zh-Hans"
    ZhHant = "zh-Hant"
