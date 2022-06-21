from django.db import models
from pydantic import BaseModel, constr, HttpUrl


class MediaTypes(models.IntegerChoices):
    Image = 1
    Video = 2


class Media(BaseModel):
    id: constr(min_length=5)
    type: MediaTypes
    url: HttpUrl
    title: constr(max_length=100)
    alt: constr(max_length=100)
