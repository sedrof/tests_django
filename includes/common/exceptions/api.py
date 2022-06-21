from django.db import models
from rest_framework import status
from rest_framework.exceptions import APIException


class InvalidDataException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "invalid input data"
    default_code = "invalid_data"


class APIErrorCodes(models.IntegerChoices):
    IncorrectPassword = 10000
    UnauthorizedService = 10001
    UnauthorizedIp = 10002
    UnapprovedWorkSchedule = 10003
    SuspendedAccount = 10004
    PausedAccount = 10005
    DeletedAccountProbation = 10006
    PasswordReuse = 10007
    # Resource / Entity Error Codes
    DuplicateEntity = 10008
    ResourceNotFound = 404
