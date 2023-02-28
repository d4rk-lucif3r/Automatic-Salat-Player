# Automatic Salat Player

This is a simple script that will automatically play Salat (Prayer) on Bluetooth Speaker at the right time, which is fetched from the [Prayer Times API](https://aladhan.com/prayer-times-api).

## How does it work?

When `salat.py` is run it will fetch the Prayer times and store in a file, after storing it will schedule the schedulers to run at each prayer time.
When the scheduler is run; it will first do the Announcement that Azaan is going to happen (this announcement is in Hindi; you can use any TTS to 
generate the file and replace the files in `announcement` folder). After the announcement it will start the Azaan.

1. Fajr Azaan has been taken from this video : https://youtu.be/iaWZ_3D6vOQ

2. Other Azaans has been taken from this video: https://youtu.be/vS0zBleiJuk

If you want you can change the azaan files also present in `azaan` folder.

## How to use

1. git clone 

2. cd Automatic-Salat-Player

3. chmod +x salat.sh && pip install -r requirements.txt

4. ./salat.sh (on Linux/Mac) will schedule a crontab for everyday at 2:00 am; On Windows, you've to schedule manually.

## How to add your Location

1. Open .env file

2. Change the value of Country, City and Method

    a. Following are the valid methods:

        0 - Shia Ithna-Ansari
        1 - University of Islamic Sciences, Karachi
        2 - Islamic Society of North America
        3 - Muslim World League
        4 - Umm Al-Qura University, Makkah
        5 - Egyptian General Authority of Survey
        7 - Institute of Geophysics, University of Tehran
        8 - Gulf Region
        9 - Kuwait
        10 - Qatar
        11 - Majlis Ugama Islam Singapura, Singapore
        12 - Union Organization islamic de France
        13 - Diyanet İşleri Başkanlığı, Turkey
        14 - Spiritual Administration of Muslims of Russia
        15 - Moonsighting Committee Worldwide (also requires shafaq parameter)
        16 - Dubai (unofficial)

3. Add Mac Address of your bluetooth

3. Save the file

## Acknowledgements

- [Prayer Times API](https://aladhan.com/prayer-times-api)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Insha Allah, I will add more features to this script in the future.



