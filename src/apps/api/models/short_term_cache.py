from django.db import models
from django_extensions.db.fields import UUIDField

from hashlib import md5
from bson import json_util

import datetime
import json


class ShortTermCache(models.Model):
    id = UUIDField(version=4, primary_key=True)
    md5 = models.CharField(max_length=128, unique=True)
    data = models.TextField()
    created = models.DateTimeField(auto_created=True, auto_now=True, default=datetime.datetime.now())

    class Meta:
        app_label = 'api'
        db_table = 'short_term_memory'


    @staticmethod
    def add_cache(key=None, data=None):
        if not all([key, data]):
            raise AttributeError("Missing key/value attributes")

        # build key into md5
        m = md5()
        m.update(key)
        key = m.hexdigest()

        # build data into json store
        if not isinstance(data, json):
            data = {data}

        data = json.dumps(data, default=json_util.default)

        ShortTermCache.objects.get_or_create(
            md5=key,
            data=data
        )
