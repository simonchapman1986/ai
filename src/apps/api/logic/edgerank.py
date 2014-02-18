import math


def calc(affinity, weight, decay):
    """
    >>> calc(12, 10, 2)
    184788.64626990957
    """

    u = math.exp(affinity)
    w = math.exp(weight)
    d = math.exp(decay)

    t = math.fsum([u, w, d])

    return t