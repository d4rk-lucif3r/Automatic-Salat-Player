#!/bin/bash

echo 'Creating Cron Job for Salat which runs at 1am everyday'
(crontab -l ; echo "0 2 * * *  python3 ${PWD}/salat.py") | crontab -

echo 'Creating Cron Job for Salat which runs at 1am everyday'

echo 'Verifying Cron Jobs'

crontab -l

echo 'Done'
