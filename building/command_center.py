# coding: utf-8
from starcraft2.building import logger
from functools import wraps


def commander_center_ready(produce_unit):
    @wraps(produce_unit)
    def _(*args, **kwargs):
        logger.error("command center ready")

        logger.info("star produce: {}".format(produce_unit.__name__[10:]))
        produce_unit(*args, **kwargs)
        logger.info("produce complete: {}".format(produce_unit.__name__[10:]))

    return _
