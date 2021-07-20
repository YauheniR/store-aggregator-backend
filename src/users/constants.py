from enum import Enum


class LanguageEnum(Enum):
    RU = "Russian"
    EN = "English"
    BY = "Belarusian"

    LANGUAGE_CHOICES = (
        ("RU", RU),
        ("EN", EN),
        ("BY", BY),
    )
