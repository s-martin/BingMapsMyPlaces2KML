
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import simplekml

print('Convert my places from Bing Maps to KML')

# set chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
# set a profile which is used every time to keep login data
chrome_options.add_argument("user-data-dir=./chromeprofile")

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.bing.com/maps/myplaces')

locations = browser.find_elements_by_class_name('bm_favoritesListItem')

# check, if run for the first time and no login data
# and therefor no locations available
if len(locations) == 0:
    print('Please login to Bing/Microsoft in the opened Chrome window.')
    response = input("Please type 'OK', if you have logged in successfully: ")
    if response != 'OK':
        print('Please start script again and login')
        browser.quit()
        exit()

locations = browser.find_elements_by_class_name('bm_favoritesListItem')
if len(locations) == 0:
    print('Could not find any locations. Exiting')
    browser.quit()
    exit()

print('Running conversion...')

kml = simplekml.Kml()

n = 0
g = 0

for element in locations:
    n = n + 1
    name, address = element.text.splitlines()
    geodata = element.get_attribute('data-entityid')
    if "_" in geodata:
        g = g + 1
        lat, lon = geodata.split('_')
        kml.newpoint(name=name, coords=[(lon, lat)], description=address)
        print(lat, ';', lon)
    else:
        print('no geo data')
        # TODO use googles geocode API to convert address to geo coordinate
    print(element.text)
    print('----')

print('Parsed ', n, 'entries, ', g, ' with geo coords')

kml.save('locations.kml')
print('Saved ', g, ' entries to locations.kml')

browser.quit()
