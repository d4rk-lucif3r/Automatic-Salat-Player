import sched
import json
import datetime
import logging
logging.basicConfig(
    filename='//Automatic-Salat-Player/logs/test.log', level=logging.INFO)

import time
prayer_times = json.load(open('//Automatic-Salat-Player/data/test.json', 'r'))


def play_azaan(prayer_name):
    logging.info(str(f'{prayer_name}, {datetime.datetime.now()}'))


scheduler = sched.scheduler(time.time, time.sleep)
for prayer, time in prayer_times.items():
    hour, minute = time.split(":")
    prayer_times[prayer] = datetime.time(
        hour=int(hour), minute=int(minute))
for prayer, time in prayer_times.items():
    prayer_time = datetime.datetime.combine(
        datetime.date.today(), time).timestamp()
    scheduler.enterabs(prayer_time, 1, play_azaan, argument=(prayer,))
    logging.info(str(" Scheduled " + prayer + " at " + str(time)))
scheduler.run()