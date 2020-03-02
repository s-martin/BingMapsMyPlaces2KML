# Convert my places from Bing Maps to Google's KML format #

This script scraps *My Places* from [Bing Maps](www.bing.com/maps) and converts them to Google's KML format

##  Prerequisites ##
1. Works with Python 3.x
2. Install selenium and simplekml
   > sudo pip install -r requirements.txt
3. Download chromedriver from https://chromedriver.chromium.org/downloads, extract and add location of chromedriver binary to `PATH`

## Usage ##
1. Start script
    > python BingMapsMyPlaces2KML.py
2. Login in your Bing/Microsoft account in the opened Chrome(driver) window
3. Type `OK` in command line
4. Takes a couple of seconds until locations.kml is saved in working directory
