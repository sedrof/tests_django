from typing import List, Type

from django.db import models


class PaymentApps(models.IntegerChoices):
    PayPal = 1
    Braintree = 2
    Square = 3
    AuthorizeNet = 4
    Stripe = 5
    TwoCheckout = 6
    Affirm = 7
    Afterpay = 8
    AliPay = 9
    Sezzle = 10
    BlueSnap = 11


class EmailMarketingApps(models.IntegerChoices):
    Mailchimp = 51
    Aweber = 52
    GetResponse = 53
    ActiveCampaign = 54
    CampaignMonitor = 55
    ConstantContact = 56
    Convertkit = 57
    Keap = 58
    Drip = 59
    Sendinblue = 60


class AdvertisingApps(models.IntegerChoices):
    GoogleAds = 101
    FacebookAds = 102


class EcommerceApps(models.IntegerChoices):
    Shopify = 120
    WooCommerce = 121


class CRMApps(models.IntegerChoices):
    Salesforce = 151
    Hubspot = 152
    ZohoCRM = 153
    Pardot = 154
    Marketo = 155
    Pipedrive = 156


class WebinarEventApps(models.IntegerChoices):
    Zoom = 201
    GotoWebinar = 202
    CiscoWebex = 203


class AnalyticsApps(models.IntegerChoices):
    GoogleAnalytics = 251
    GoogleTagManager = 252


class SocialMediaApps(models.IntegerChoices):
    Facebook = 301
    Instagram = 302
    YouTube = 303
    LinkedIn = 304
    Twitter = 305


class ShippingFulfilmentApps(models.IntegerChoices):
    Shipbob = 351
    Easyship = 352
    ShipStation = 353


class TaxComplianceApps(models.IntegerChoices):
    TaxCloud = 401
    Avalara = 402


class OtherApps(models.IntegerChoices):
    Zapier = 451


THIRD_PARTY_APPS: List[Type[models.IntegerChoices]] = [
    PaymentApps,
    EmailMarketingApps,
    AdvertisingApps,
    EcommerceApps,
    CRMApps,
    WebinarEventApps,
    AnalyticsApps,
    SocialMediaApps,
    ShippingFulfilmentApps,
    TaxComplianceApps,
    OtherApps,
]
