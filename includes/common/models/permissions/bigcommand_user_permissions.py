"""
Custom permissions for restricting actions available to subusers.
All permissions in BigCommand applications will be managed in the
user model.
"""
from typing import List, Type, TypedDict

from django.db.models import IntegerChoices


class AccountPermissions(IntegerChoices):
    ChangeBusinessInformation = 1
    ChangeSecuritySetting = 2
    ManageBilling = 3
    ManageThirdPartyIntegrations = 4
    ManageUsers = 5
    ManageRoles = 6
    ViewAPIData = 7
    ManageAPIData = 8
    ManageDomains = 9
    ManageSitePixels = 10
    ManageAccountNotification = 11
    ReceiveAccountNotification = 12


class AdiloPermissions(IntegerChoices):
    ViewAdiloDashboard = 51
    ManageAccountDashboard = 52
    ManageAdiloProjects = 53
    UploadMedia = 54
    CustomizeMedia = 55
    DeleteVideos = 56
    ManageAdiloChannels = 57
    ManageSnapByte = 58
    ViewAdiloAnalytics = 59
    ChangeAdiloSettings = 60
    ManageAdiloNotification = 61
    ReceiveAdiloNotification = 62


class BigDrivePermissions(IntegerChoices):
    ViewBigDriveDashboard = 101
    ManageBigDriveDashboard = 102
    ManageSpaces = 103
    UploadFilesAndFolders = 104
    ViewFilesAndFolders = 105
    ShareFilesAndFolders = 106
    TrashAndDeleteFilesAndFolders = 107
    ManageFileRequests = 108
    ManageFileTransfers = 109
    SignDocuments = 110
    ManageSignatureRequests = 111
    ViewBigDriveAnalytics = 112
    ChangeBigDriveSettings = 113
    ManageBigDriveNotification = 114
    ReceiveBigDriveNotification = 115


class BigPartnerPermissions(IntegerChoices):
    ViewBigPartnerDashboard = 151
    ManagePartnerInformation = 152
    ManageBigPartnerNotification = 153
    ReceivePartnerNotification = 154


class BoomAffiliatePermissions(IntegerChoices):
    ViewBoomAffiliateDashboard = 201
    ManageBoomAffiliateDashboard = 202
    ManagePromotions = 203
    ManageAffiliateProducts = 204
    ManageAffiliates = 205
    ManagePayouts = 206
    ViewBoomAffiliateAnalytics = 207
    ChangeBoomAffiliateSettings = 208
    ManageBoomAffiliateNotification = 209
    ReceiveBoomAffiliateNotification = 210


class BoomFrontPermissions(IntegerChoices):
    ViewBoomFrontDashboard = 251
    ManageBoomFrontDashboard = 252
    ManageProducts = 253
    ManageCollections = 254
    ManageDigitalLicenses = 255
    ManageCoupons = 256
    ManageReviews = 257
    ManageOrdersAndSubscriptions = 258
    ManageTransactions = 259
    ManageAbandonedCart = 260
    ManageStores = 261
    ManageFunnels = 262
    ManageChannels = 263
    ExportAndImportFunnelsAndStores = 264
    ViewBoomFrontAnalytics = 265
    ChangeBoomFrontSettings = 266
    ManageBoomFrontNotification = 267
    ReceiveBoomFrontNotification = 268


class ContactsPermissions(IntegerChoices):
    ViewContactsDashboard = 301
    ManageContactsDashboard = 302
    ViewContactDetail = 303
    EditContact = 304
    BulkImportContacts = 305
    BulkExportContacts = 306
    AddAContact = 307
    UnsubscribeContact = 308
    ManageTags = 309
    ManageSegments = 310
    DeleteContact = 311
    ViewContactsAnalytics = 312
    ChangeContactsSettings = 313


class CorinaPermissions(IntegerChoices):
    ViewCorinaDashboard = 351
    ManageCorinaDashboard = 352
    ManageBoards = 353
    ManageTasks = 354
    ManageEvents = 355
    ViewCorinaAnalytics = 356
    ChangeCorinaSettings = 357
    ManageCorinaNotification = 358
    ReceiveCorinaNotification = 359


class HelpCenterPermissions(IntegerChoices):
    PostInCommunity = 401
    PostFeatureRequest = 402


class HomePermissions(IntegerChoices):
    ViewSummaryPerformanceReport = 451


class HuulaPermissions(IntegerChoices):
    ViewHuulaDashboard = 501
    ManageHuulaDashboard = 502
    ManageWebinars = 503
    ManageMeetings = 504
    ViewHuulaAnalytics = 505
    ChangeHuulaSettings = 506
    ManageHuulaNotification = 507
    ReceiveHuulaNotification = 608


class InboxBirdPermissions(IntegerChoices):
    ViewInboxBirdDashboard = 551
    ManageInboxBirdDashboard = 552
    ManageEmailCampaigns = 553
    ManageSocialCampaigns = 554
    ManageAutomatedCallAndSMS = 555
    ManagePushNotifications = 556
    ManageSiteMessaging = 557
    ViewAndManageConversations = 558
    ManageLandingAndLeadPages = 559
    ManagePipelineDeals = 560
    ManageLists = 561
    ManageForms = 562
    ChangeProfileBuilderSettings = 563
    ChangeListCleanerSettings = 564
    ManageAutomations = 565
    ViewInboxBirdAnalytics = 566
    ChangeInboxBirdSettings = 567
    ManageInboxBirdNotification = 568
    ReceiveInboxBirdNotification = 569


class PortalPermissions(IntegerChoices):
    ManageOrdersAndSubscriptions = 601
    ManageEmailSubscriptions = 602
    ManageEvents = 603
    ViewSignedDocuments = 604


class uVendiPermissions(IntegerChoices):
    ...


# Some permissions can be inherited from a less restrictive permission.
PERMISSION_INHERITANCE: dict[IntegerChoices, list[IntegerChoices]] = {
    AccountPermissions.ViewAPIData: [AccountPermissions.ManageAPIData],
    ContactsPermissions.ViewContactDetail: [
        ContactsPermissions.AddAContact,
        ContactsPermissions.EditContact,
        ContactsPermissions.DeleteContact,
    ],
}

SUBUSER_PERMISSIONS: List[Type[IntegerChoices]] = [
    AccountPermissions,
    AdiloPermissions,
    BigDrivePermissions,
    BigPartnerPermissions,
    BoomAffiliatePermissions,
    BoomFrontPermissions,
    ContactsPermissions,
    CorinaPermissions,
    HelpCenterPermissions,
    HomePermissions,
    HuulaPermissions,
    InboxBirdPermissions,
    PortalPermissions,
    uVendiPermissions,
]


class RolePermissionMapping(TypedDict):
    name: str
    description: str
    permissions: List[IntegerChoices]


DEFAULT_ROLES: List[RolePermissionMapping] = [
    {
        "name": "admin",
        "description": "Has full access to all account features and resources, but cannot delete account.",
        "permissions": [perm for perms in SUBUSER_PERMISSIONS for perm in perms],
    },
    {
        "name": "store manager",
        "description": "Can view and manage products, collections, inventory, coupons, digital licenses, product "
        "reviews, orders and subscriptions, seller settings, shipping and tax.",
        "permissions": [
            BoomFrontPermissions.ViewBoomFrontDashboard,
            BoomFrontPermissions.ManageProducts,
            BoomFrontPermissions.ManageCollections,
            BoomFrontPermissions.ManageCoupons,
            BoomFrontPermissions.ManageDigitalLicenses,
            BoomFrontPermissions.ManageReviews,
            BoomFrontPermissions.ManageOrdersAndSubscriptions,
            BoomFrontPermissions.ChangeBoomFrontSettings,
        ],
    },
    {
        "name": "sales manager",
        "description": "Can view and manage stores, funnels, sales channels, deal pipelines, orders and subscription, "
        "transaction, abandoned checkout and campaign/promotion tools.",
        "permissions": [
            BoomFrontPermissions.ViewBoomFrontDashboard,
            BoomFrontPermissions.ManageBoomFrontDashboard,
            BoomFrontPermissions.ViewBoomFrontAnalytics,
            BoomFrontPermissions.ManageStores,
            BoomFrontPermissions.ManageFunnels,
            BoomFrontPermissions.ManageChannels,
            BoomFrontPermissions.ManageOrdersAndSubscriptions,
            BoomFrontPermissions.ManageTransactions,
            BoomFrontPermissions.ManageAbandonedCart,
            BoomFrontPermissions.ManageCoupons,
            BoomFrontPermissions.ViewBoomFrontAnalytics,
            InboxBirdPermissions.ViewInboxBirdDashboard,
            InboxBirdPermissions.ManageInboxBirdDashboard,
            InboxBirdPermissions.ManagePipelineDeals,
            InboxBirdPermissions.ManageLandingAndLeadPages,
            InboxBirdPermissions.ManageEmailCampaigns,
            InboxBirdPermissions.ManageAutomations,
            InboxBirdPermissions.ManageForms,
            InboxBirdPermissions.ManageSiteMessaging,
            InboxBirdPermissions.ManageSocialCampaigns,
            InboxBirdPermissions.ManagePushNotifications,
            InboxBirdPermissions.ManageAutomatedCallAndSMS,
            InboxBirdPermissions.ViewAndManageConversations,
            InboxBirdPermissions.ManageLists,
            InboxBirdPermissions.ViewInboxBirdAnalytics,
            ContactsPermissions.AddAContact,
            ContactsPermissions.DeleteContact,
            ContactsPermissions.EditContact,
            ContactsPermissions.ManageTags,
            ContactsPermissions.ManageSegments,
            ContactsPermissions.BulkImportContacts,
        ],
    },
    {
        "name": "website manager",
        "description": "Can create and edit stores, funnels, landing and lead pages.",
        "permissions": [
            BoomFrontPermissions.ManageStores,
            BoomFrontPermissions.ManageFunnels,
            InboxBirdPermissions.ManageLandingAndLeadPages,
        ],
    },
    {
        "name": "billing manager",
        "description": "",
        "permissions": [AccountPermissions.ManageBilling],
    },
    {
        "name": "payment manager",
        "description": "",
        "permissions": [BoomFrontPermissions.ManageOrdersAndSubscriptions],
    },
    {
        "name": "marketing manager",
        "description": "",
        "permissions": [InboxBirdPermissions.ManageEmailCampaigns],
    },
    {
        "name": "customer relationship manager",
        "description": "",
        "permissions": [InboxBirdPermissions.ManagePipelineDeals],
    },
    {
        "name": "affiliate manager",
        "description": "",
        "permissions": [BoomAffiliatePermissions.ManageAffiliates],
    },
    {
        "name": "digital assets manager",
        "description": "",
        "permissions": [BigDrivePermissions.ManageSpaces],
    },
    {
        "name": "project manager",
        "description": "",
        "permissions": [CorinaPermissions.ManageTasks],
    },
]
