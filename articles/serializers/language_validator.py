from collections import Mapping

from django.utils.translation import gettext as _
from rest_framework import exceptions

from includes.common.supported_languages import SupportedLanguages


class LanguageValidator:
    def validate(self, data: Mapping) -> Mapping:
        if (
            (lang := data.get("language"))
            and lang != SupportedLanguages.EN
            and not data.get("englishVersion")
        ):
            raise exceptions.ValidationError(
                {
                    "englishVersion": _(
                        "english version id required for non-english contents"
                    )
                }
            )
        return data
