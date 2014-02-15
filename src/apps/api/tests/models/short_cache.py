from django.test import TestCase

from apps.api.models import ShortTermCache


class TestShortCacheMemory(TestCase):

    KEY = 'abcdefghijklmnopqrstuvwxyz'
    DATA = 'value'
    DATA_JSON = {'key':'value'}

    def test_cache_store_no_json(self):

        ShortTermCache.add_cache(
            key=self.KEY,
            data=self.DATA
        )

        sc = ShortTermCache.objects.get(key=self.KEY)

        self.assertEqual(
            self.DATA,
            sc.data
        )
