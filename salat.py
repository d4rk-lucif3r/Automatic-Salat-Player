import os
from dotenv import load_dotenv
load_dotenv()

import requests
import json
from pprint import pprint

from salat_scheduler import schedule_salat
import logging
import time


logging.basicConfig(
    filename='/home/pi/Automatic-Salat-Player/logs/salat.log', level=logging.INFO)


def get_salat_times():
    response = requests.get(
        f"http://api.aladhan.com/v1/timingsByCity?city={os.getenv('City')}&country={os.getenv('Country')}&method={os.getenv('Method')}")
    keys = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
    if response.status_code == 200:
        response_dict = response.json()['data']['timings']
        logging.info(' Salat times fetched')
        return {key: response_dict[key] for key in keys}
    else:
        logging.error(' Error fetching salat times')
        return None


if __name__ == '__main__':
    logging.info(f' Assalamu alaikum, fetching Salat times for today at {time.ctime()}')
    data = get_salat_times()
    if data is None:
        logging.info(' Error fetching salat times; will use last saved times')
        data = json.load(open('/home/pi/Automatic-Salat-Player/data/salat_times.json', 'r'))
    else:
        with open('/home/pi/Automatic-Salat-Player/data/salat_times.json', 'w') as f:
            json.dump(data, f)
        logging.info(' Today\'s Salat times saved')
    logging.info(' Today\'s Salat times:')
    logging.info( data)
    time.sleep(5)
    logging.info(' Scheduling Salat')
    scheduler = schedule_salat()
    scheduler.run()
