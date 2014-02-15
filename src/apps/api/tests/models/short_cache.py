from django.test import TestCase

from apps.api.models import ShortTermCache

from hashlib import md5

import cPickle


class TestShortCacheMemory(TestCase):

    KEY = 'abcdefghijklmnopqrstuvwxyz'
    DATA = 'value'
    DATA_JSON = {'key':'value'}

    def test_cache_store_no_json_create(self):

        data, created = ShortTermCache.add_cache(
            key=self.KEY,
            data=self.DATA
        )

        # build the key
        # build key into md5
        m = md5()
        m.update(self.KEY)
        key = m.hexdigest()

        sc = ShortTermCache.objects.get(md5=key)

        # confirm we are creating a new object
        self.assertTrue(created)

        self.assertEqual(
            self.DATA,
            cPickle.loads(str(sc.data))['cache']
        )

    def test_cache_store_json_create(self):

        data, created = ShortTermCache.add_cache(
            key=self.KEY,
            data=self.DATA_JSON
        )

        # build the key
        # build key into md5
        m = md5()
        m.update(self.KEY)
        key = m.hexdigest()

        sc = ShortTermCache.objects.get(md5=key)

        # confirm we are creating a new object
        self.assertTrue(created)

        self.assertEqual(
            self.DATA_JSON,
            cPickle.loads(str(sc.data))
        )

    def test_cache_store_no_json_read(self):

        # build the key
        # build key into md5
        m = md5()
        m.update(self.KEY)
        key = m.hexdigest()

        data = ShortTermCache.objects.create(
            md5=key,
            data=cPickle.dumps({'cache': self.DATA})
        )

        data, created = ShortTermCache.add_cache(
            key=self.KEY,
            data=self.DATA
        )

        # confirm we are creating a new object
        self.assertFalse(created)

        self.assertEqual(
            self.DATA,
            cPickle.loads(str(data))['cache']
        )


    def test_cache_store_json_read(self):

        # build the key
        # build key into md5
        m = md5()
        m.update(self.KEY)
        key = m.hexdigest()

        data = ShortTermCache.objects.create(
            md5=key,
            data=cPickle.dumps(self.DATA_JSON)
        )

        data, created = ShortTermCache.add_cache(
            key=self.KEY,
            data=self.DATA_JSON
        )

        # confirm we are creating a new object
        self.assertFalse(created)

        self.assertEqual(
            self.DATA_JSON,
            cPickle.loads(str(data))
        )
