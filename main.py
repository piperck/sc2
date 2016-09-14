# coding: utf-8
import time
from tqdm import tqdm
from building.starport import starport_ready
from building.command_center import commander_center_ready


@starport_ready("Banshee Cloaking Field")
def produce_a_viking(seconds=30):
    for i in tqdm(xrange(seconds)):
        time.sleep(1)


@commander_center_ready
def produce_a_scv(seconds=12):
    for i in tqdm(xrange(seconds)):
        time.sleep(1)


if '__main__' == __name__:
    # produce_a_viking()
    produce_a_scv()
