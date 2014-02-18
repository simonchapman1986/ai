from models.short_cache import *

from apps.api.models import ShortTermCache

from django.conf import settings

def quick_load():
    """
    >>> quick_load()
    1
    """
    import json

    with open(settings.PROJECT_ROOT+'/dictionary.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        for k in d:
            data, created = ShortTermCache.add_cache(
                key=k,
                data={k.encode('utf-8'):d[k].encode('utf-8')}
            )
            print created, data