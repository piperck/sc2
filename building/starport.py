# coding: utf-8
import time
from tqdm import tqdm
from functools import wraps
from starcraft2.building import logger


def starport_upgrade(SCUpgrade):
    logger.info("starport upgrade: {0}".format(SCUpgrade))

    if SCUpgrade == "High Capacity Fuel Tanks":
        for i in tqdm(xrange(57)):
            time.sleep(1)
    elif SCUpgrade == "Explosive Shrapnel Shells":
        for i in tqdm(xrange(79)):
            time.sleep(1)
    elif SCUpgrade == "Corvid Reactor":
        for i in tqdm(xrange(79)):
            time.sleep(1)
    elif SCUpgrade == "Banshee Cloaking Field":
        for i in tqdm(xrange(79)):
            time.sleep(1)
    elif SCUpgrade == "Hyperflight Rotors":
        for i in tqdm(xrange(96)):
            time.sleep(1)
    elif SCUpgrade == "Advanced Ballistics":
        for i in tqdm(xrange(79)):
            time.sleep(1)

    logger.info("starport upgrade complete: {0}".format(SCUpgrade))


def starport_ready(SCUpgrade=None):

    def starport_decrator(produce_unit):
        @wraps(produce_unit)
        def _(*args, **kwargs):
            try:
                if SCUpgrade:
                    starport_upgrade(SCUpgrade)
                logger.info("starport ready")

                logger.info("star produce: {}".format(produce_unit.__name__[10:]))
                produce_unit(*args, **kwargs)
                logger.info("produce complete: {}".format(produce_unit.__name__[10:]))
            except Exception as e:
                logger.error(e.message)
        return _

    return starport_decrator
