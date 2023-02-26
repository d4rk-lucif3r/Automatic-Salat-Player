import json
import pygame
import sched
import time
import logging
import datetime
import subprocess


logging.basicConfig(
    filename='/home/pi/Automatic-Salat-Player/logs/salat.log', level=logging.INFO)
scheduler = sched.scheduler(time.time, time.sleep)


def play_azaan(prayer_name):
    subprocess.run(['bluetoothctl', 'power', 'on'])
    subprocess.run(['bluetoothctl', 'connect', 'B4:B7:42:C3:50:76'])
    pygame.mixer.init()
    logging.info(str(" Its time for " + prayer_name + ""))
    pygame.mixer.music.load(
        f'/home/pi/Automatic-Salat-Player/announcements/{prayer_name.lower()}_announcement_hindi.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    time.sleep(2)
    pygame.mixer.music.load('/home/pi/Automatic-Salat-Player/azaan/azaan_fajr.mp3') if prayer_name == 'Fajr' else pygame.mixer.music.load(
        '/home/pi/Automatic-Salat-Player/azaan/azaan.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    else:
        logging.info(str(" Azaan for " + prayer_name + " is over"))
        pygame.mixer.stop()
    subprocess.run(['bluetoothctl', 'power', 'off'])

def schedule_salat():
    with open('/home/pi/Automatic-Salat-Player/data/salat_times.json') as f:
        prayer_times = json.load(f)
    for prayer, time1 in prayer_times.items():
        hour, minute = time1.split(":")
        prayer_times[prayer] = datetime.time(
            hour=int(hour), minute=int(minute))
    for prayer, time1 in prayer_times.items():
        prayer_time = datetime.datetime.combine(
            datetime.date.today(), time1).timestamp()
        if prayer_time > time.time():    
            scheduler.enterabs(prayer_time, 1, play_azaan, argument=(prayer,))
            logging.info(str(" Scheduled " + prayer + " at " + str(time1)))
    return scheduler
