from django.conf import settings
from django.db.models import Sum
from django.db.models.query import F
from django.db.models.functions import Length
from zerver.models import UserProfile

from typing import Text, Dict, Optional

class ConfigError(Exception):
    pass

def get_bot_config(bot_profile: UserProfile) -> Dict[Text, Text]:
    return {}
