from apps.api.models import ShortTermCache

from apps.api.logic import edgerank

from django.conf import settings


class Decision(object):
    """
    >>> d = Decision(item='hello')
    """

    def __init__(self, item):

        # do i know this item?
        # check short memory cache..
        s = ShortTermCache.objects.filter(data__icontains=item).order_by('-created')

        c=0
        ranks = {}
        for i in s:
            # let us establish its importance
            # calc weight - see proportion of string that is the value
            length = len(i.data)
            length_i = len(item)
            w = length_i/length

            e = edgerank.calc(
                affinity=settings.AFFINITY['SHORT_TERM'],
                weight=w,
                decay=c
            )

            ranks[e] = i
            c+=1

        sortedlist = [(k, ranks[k]) for k in sorted(ranks)]

        print sortedlist
        print sortedlist[0][1].data

        # todo: search long term memory
