import uuid

from articles.models.common import Member, TitleSlugFields
from articles.models.tags import Tag
from articles.models.topics import Topic
from articles.models.categories import Category
from django.utils import timezone

from includes.common.supported_languages import SupportedLanguages


def initialize_member():
    return Member.objects.create(
        fullName="test1",
        emailAddress="abcd@abcd.com",
        joinDate=timezone.now(),
        bigCommandId=str(uuid.uuid4()),
        publicName="test_public_name",
        # roles
    )



def initialize_tag(name):
    return Tag.objects.create(
        language=SupportedLanguages.EN, name=name
    )



def initialize_category():

    return Category.objects.create(
        description="test_describtion_1",
        app="22",
        language="EN",
        title="test_slug_field",
    )



def initialize_topic():
    return Topic.objects.create(
        description="test_topic",
        category=initialize_category(),
        title='test_topic_title',
        language=SupportedLanguages.EN
    )


def initialize_slug_field():
    return TitleSlugFields.objects.create(
        description="test_describtion",
        slug='test_slug_field',
    )